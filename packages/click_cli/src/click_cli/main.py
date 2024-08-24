from sys import stderr
from textwrap import indent

import click
from msgspec import ValidationError

from emptypt.action import foo
from emptypt.error_handlers import CaptureInvalidConfigExit

from .interface import ActionConfig

__all__ = ("run_cli",)


def handle_validation_error(ve: ValidationError) -> None:
    msgs = []
    for e in ve.errors():
        if ctx := e.get("ctx"):
            new_msg = str(ctx["error"])
        else:
            new_msg = e["msg"]
        msgs.append(new_msg)
    error_msgs = "\n".join(msgs)
    msg = "Invalid command:\n" + indent(error_msgs, prefix="- ")
    print(msg, end="\n\n", file=stderr)
    return


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--io_arg1", is_flag=True, help="The first IO configuration entry.")
@click.option(
    "--filter_arg1",
    is_flag=True,
    help="The first filtering configuration entry.",
)
@click.option("--quiet", is_flag=True, help="Whether to suppress console output.")
@click.option("--debug", is_flag=True, help="Whether to run debug diagnostics.")
def run_cli(io_arg1, filter_arg1, quiet, debug) -> list:
    try:
        config = ActionConfig(
            io_arg1=io_arg1,
            filter_arg1=filter_arg1,
            quiet=quiet,
            debug=debug,
        )
    except ValidationError as ve:
        handle_validation_error(ve)
        with CaptureInvalidConfigExit():
            print("(Failed)")
            raise NotImplementedError("TODO: make this show help text")
            pass  # configure(argv=["-h"])
    else:
        return foo(config)
