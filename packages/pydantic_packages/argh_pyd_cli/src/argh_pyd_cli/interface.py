from pydantic import BaseModel, Field

__all__ = ("ActionConfig",)


def desc(default, description: str) -> Field:
    """Construct a `pydantic.Field` with a description"""
    return Field(default, description=description)


class ActionConfig(BaseModel):
    """Configure input filtering and output display."""

    io_arg1: bool = desc(False, "Example IO flag")
    filter_arg1: bool = desc(False, "Example filter flag")
    quiet: bool = desc(False, "Run silently")
    debug: bool = desc(False, "Run debug diagnostics")
    undocumented: bool = False
