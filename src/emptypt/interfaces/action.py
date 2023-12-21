from msgspec import Struct

# from .debug import DebugConfig
# from .display import DisplayConfig

__all__ = ("ActionConfig",)


# class FilterConfig(Struct):
#     filter_arg1: bool = False
#
#
# class IOConfig(Struct):
#     io_arg1: bool = False


class ActionConfig(Struct):
    """
    Configure input filtering and output display.

      :param io_arg1: The first IO configuration entry.
      :param filter_arg1: The first filtering configuration entry.
      :param quiet: Whether to suppress console output.
      :param debug: Whether to run debug diagnostics.
    """

    io_arg1: bool = False
    filter_arg1: bool = False
