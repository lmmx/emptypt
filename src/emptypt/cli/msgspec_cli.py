from sys import stderr
from textwrap import indent

import defopt
from msgspec import ValidationError

from ..core.action import foo
from ..core.error_handlers import CaptureInvalidConfigExit
from ..interfaces import ActionConfig

__all__ = ("run_cli",)


def configure(**defopt_kwargs) -> ActionConfig:
    """Runs defopt CLI using `sys.argv`, raises `SystemExit` if the config is invalid"""
    defopt_kwargs.update(no_negated_flags=True, show_types=True)
    return defopt.run(ActionConfig, **defopt_kwargs)


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


def run_cli() -> None:
    try:
        config = configure()
    except ValidationError as ve:
        handle_validation_error(ve)
        with CaptureInvalidConfigExit():
            configure(argv=["-h"])
    else:
        _ = foo(config)
        return None
