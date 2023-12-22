from ..interfaces.action import ActionConfig
from .minimal_op import bar

__all__ = ("foo",)


def foo(config: ActionConfig | dict = {}):
    return bar()
