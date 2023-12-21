from msgspec import Struct

__all__ = ("DebugConfig",)


class DebugConfig(Struct):
    """Put any debug settings here"""

    debug: bool = False
