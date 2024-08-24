from __future__ import annotations

from argparse import ArgumentParser
from collections.abc import Callable
from textwrap import dedent
from typing import Annotated, get_args, get_origin, get_type_hints

import argh
import msgspec

from emptypt.action import foo
from emptypt.error_handlers import CaptureInvalidConfigExit
from emptypt.errors import EntryptMisconfigurationExit

from .interface import DocstringActionConfig

__all__ = ("run_cli",)


def stringify_hint(type_hint) -> str:
    match type_hint:
        case type():
            hint = type_hint.__name__
        case _:
            hint = str(type_hint)
    return hint


def parse_docstring(doc: str) -> tuple[str, dict[str, str]]:
    body = dedent(doc).strip("\n")
    first_param_idx = body.find(":param ")
    preamble_end_idx = body.rfind("\n", 0, first_param_idx)
    preamble = body[:preamble_end_idx].strip()
    paramble = dedent(body[preamble_end_idx:]).strip("\n")
    param_docs = {}
    if param_entries := paramble.split(":param ")[1:]:
        for entry in param_entries:
            param, success, desc = entry.partition(":")
            if success:
                multiline_desc = map(str.strip, desc.strip().splitlines())
                description = " ".join(multiline_desc)
                param_docs[param] = description
    return preamble, param_docs


def populate_parser_descriptions(parser: ArgumentParser, struct: Callable) -> None:
    hints = get_type_hints(struct, include_extras=True)
    parser_description, parsed_ds = parse_docstring(struct.__doc__)
    parser.description = parser_description
    for action in parser._actions:
        if (flag := action.dest) in struct.__struct_fields__:
            if get_origin(hints[flag]) is Annotated:
                type_hint = get_args(hints[flag])[0]
            else:
                type_hint = hints[flag]
            hint = stringify_hint(type_hint)
            match action.default:
                case msgspec._core.Factory() as factory_manager:
                    # The msgspec default factory didn't get instantiated by argh
                    action.default = factory_manager.factory()
            desc: str | None = parsed_ds.get(flag)
            flag_meta = f"(type: {hint}, default: {action.default})"
            action.help = " ".join(filter(None, [desc, flag_meta]))


def dispatch_command(cmd: Callable, **argh_kwargs):
    """
    Replace the argh.dispatch function (str return type) specifically, by exitting early
    without calling `run_endpoint_function`, and just calling it ourselves.

    `argh_kwargs` are optional parameters for `argh.parse_and_resolve`, see its docs:

        argv: list[str] | None = None
        completion: bool = True
        namespace: argparse.Namespace | None = None
        skip_unknown_args: bool = False
    """
    parser = ArgumentParser()
    argh.set_default_command(parser, cmd)
    populate_parser_descriptions(parser, cmd)
    with CaptureInvalidConfigExit():
        _, namespace = argh.parse_and_resolve(parser=parser, **argh_kwargs)
    ns_kwargs = vars(namespace)
    ns_kwargs.pop("_functions_stack")
    return cmd(**ns_kwargs)


def configure(**argh_kwargs) -> DocstringActionConfig:
    """Runs argh CLI using `sys.argv`, raises `SystemExit` if the config is invalid"""
    return dispatch_command(DocstringActionConfig, **argh_kwargs)


def run_cli() -> None:
    try:
        config = configure()
    except EntryptMisconfigurationExit:
        configure(argv=["-h"])
    else:
        _ = foo(config)
        return None
