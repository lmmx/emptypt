from argparse import ArgumentParser
from typing import Callable

import argh

from ..core.action import foo
from ..core.errors import EntryptMisconfigurationExit
from ..interfaces import ActionConfig

__all__ = ("run_cli",)


def populate_parser_descriptions(parser: ArgumentParser, struct: Callable) -> None:
    for action in parser._actions:
        if (flag := action.dest) in struct.__struct_fields__:
            annotation = struct.__annotations__[flag]
            try:
                hint = annotation.__args__[0].__name__
                desc = annotation.__metadata__[0].description
                action.help = f"{desc} (type: {hint}, default: {action.help})"
            except AttributeError:
                hint = annotation.__name__
                action.help = f"(type: {hint}, default: {action.help})"


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
    try:
        _, namespace = argh.parse_and_resolve(parser=parser, **argh_kwargs)
    except SystemExit as exc:
        if exc.code != 0:
            raise EntryptMisconfigurationExit()
        else:
            raise  # Do not intercept if passed `-h`
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
