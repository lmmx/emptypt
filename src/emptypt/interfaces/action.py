from typing import Annotated

from msgspec import Meta, Struct

__all__ = ("ActionConfig",)


def field(typ, description: str):
    """Annotate a `msgspec.Struct` field with a description"""
    return Annotated[typ, Meta(description=description)]


class ActionConfig(Struct):
    """Configure input filtering and output display."""

    io_arg1: field(bool, "Example IO flag") = False
    filter_arg1: field(bool, "Example filter flag") = False
    quiet: field(bool, "Run silently") = False
    debug: field(bool, "Run debug diagnostics") = False
    undocumented: bool = False
