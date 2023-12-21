from msgspec import Struct

__all__ = ("DisplayConfig",)


class DisplayConfig(Struct):
    """Put any display settings here"""

    quiet: bool = False
