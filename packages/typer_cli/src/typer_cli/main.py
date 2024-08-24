from sys import stderr
from textwrap import indent

import typer
from msgspec import ValidationError

from emptypt.action import foo
from emptypt.interfaces.action import ActionConfig

__all__ = ("run_cli",)

app = typer.Typer(help="CLI tool made with Typer")


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


@app.command()  # doesn't work?
def run_cli(debug: bool = False) -> None:
    try:
        config = ActionConfig(debug=debug)
    except ValidationError as ve:
        handle_validation_error(ve)
    else:
        _ = foo(config)
        return None
