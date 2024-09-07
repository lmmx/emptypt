from typing import Annotated

from pydantic import BaseModel, Field

__all__ = ("ActionConfig",)


class ActionConfig(Struct):
    """Configure input filtering and output display."""

    io_arg1: bool = Field(False, description="Example IO flag")
    filter_arg1: bool = Field(False, description="Example filter flag")
    quiet: bool = Field(False, description="Run silently")
    debug: bool = Field(False, description="Run debug diagnostics")
    undocumented: bool = False
