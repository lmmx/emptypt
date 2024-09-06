from typing import Annotated

from msgspec import Meta, Struct

__all__ = ("ActionConfig",)


def desc(typ, description: str):
    """Annotate a `msgspec.Struct` field with a description"""
    return Annotated[typ, Meta(description=description)]


class ActionConfig(Struct):
    """Configure input filtering and output display."""

    io_arg1: desc(bool, "Example IO flag") = False
    filter_arg1: desc(bool, "Example filter flag") = False
    quiet: desc(bool, "Run silently") = False
    debug: desc(bool, "Run debug diagnostics") = False
    undocumented: bool = False
