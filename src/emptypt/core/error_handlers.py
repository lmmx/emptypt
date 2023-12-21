from contextlib import AbstractContextManager
from types import TracebackType

from .errors import EntryptMisconfigurationExit

__all__ = "CaptureInvalidConfigExit"


class CaptureInvalidConfigExit(AbstractContextManager):
    def __exit__(
        self,
        __exc_type: type[SystemExit] | None,
        __exc_value: SystemExit | None,
        __traceback: TracebackType | None,
    ) -> bool | None:
        if __exc_type is SystemExit:
            raise FugitMisconfigurationExit()
        else:
            return super().__exit__(__exc_type, __exc_value, __traceback)
