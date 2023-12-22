from msgspec import Struct

__all__ = ("DocstringActionConfig",)


class DocstringActionConfig(Struct):
    """
    Configure input filtering and output display.

      :param io_arg1: Example IO flag
      :param filter_arg1: Example filter flag
      :param quiet: Run silently
      :param debug: Run debug diagnostics
    """

    io_arg1: bool = False
    filter_arg1: bool = False
    quiet: bool = False
    debug: bool = False
    undocumented: bool = False
