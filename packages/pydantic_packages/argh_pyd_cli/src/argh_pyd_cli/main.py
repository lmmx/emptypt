from __future__ import annotations

from argparse import ArgumentParser
from collections.abc import Callable
from typing import Annotated, get_args, get_origin, get_type_hints, TypeVar

import argh
from pydantic import BaseModel

from emptypt.action import foo
from emptypt.error_handlers import CaptureInvalidConfigExit
from emptypt.errors import EntryptMisconfigurationExit

from .interface import ActionConfig

__all__ = ("run_cli",)

M = TypeVar("M", bound=BaseModel)

def stringify_hint(type_hint) -> str:
    match type_hint:
        case type():
            hint = type_hint.__name__
        case _:
            hint = str(type_hint)
    return hint


def populate_parser_descriptions(parser: ArgumentParser, model: type[M]) -> None:
    hints = get_type_hints(model, include_extras=True)
    for action in parser._actions:
        if (flag := action.dest) in model.model_fields:
            field = model.model_fields[flag]
            hint = stringify_hint(hints[flag])
            desc = (field.description or "") + " "
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
        return foo(config)
