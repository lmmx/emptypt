from __future__ import annotations

from argparse import ArgumentParser
from collections.abc import Callable
from typing import Annotated, get_args, get_origin, get_type_hints

import argh
import msgspec

from emptypt.action import foo
from emptypt.error_handlers import CaptureInvalidConfigExit
from emptypt.errors import EntryptMisconfigurationExit

from .interface import ActionConfig

__all__ = ("run_cli",)


def stringify_hint(type_hint) -> str:
    match type_hint:
        case type():
            hint = type_hint.__name__
        case _:
            hint = str(type_hint)
    return hint


def populate_parser_descriptions(parser: ArgumentParser, struct: Callable) -> None:
    hints = get_type_hints(struct, include_extras=True)
    for action in parser._actions:
        if (flag := action.dest) in struct.__struct_fields__:
            if get_origin(hints[flag]) is Annotated:
                type_hint, meta = get_args(hints[flag])
                hint = stringify_hint(type_hint)
                desc = meta.description + " "
            else:
                # If the type is unannotated no meta so no description
                hint = stringify_hint(hints[flag])
                desc = ""
            match action.default:
                case msgspec._core.Factory() as factory_manager:
                    # The msgspec default factory didn't get instantiated by argh
                    action.default = factory_manager.factory()
            action.help = f"{desc}(type: {hint}, default: {action.default})"


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


def configure(**argh_kwargs) -> ActionConfig:
    """Runs argh CLI using `sys.argv`, raises `SystemExit` if the config is invalid"""
    return dispatch_command(ActionConfig, **argh_kwargs)


def run_cli() -> None:
    try:
        config = configure()
    except EntryptMisconfigurationExit:
        configure(argv=["-h"])
    else:
        _ = foo(config)
        return None
