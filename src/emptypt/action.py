from .minimal_op import bar

__all__ = ("foo",)


def foo(config: dict = {}):
    return bar()
