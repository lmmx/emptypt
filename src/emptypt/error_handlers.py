from contextlib import AbstractContextManager
from types import TracebackType

from .errors import EntryptMisconfigurationExit

__all__ = ("CaptureInvalidConfigExit",)


class CaptureInvalidConfigExit(AbstractContextManager):
    def __exit__(
        self,
        exc_type: type[SystemExit] | None,
        exc_value: SystemExit | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        if exc_type is SystemExit and exc_value.code != 0:
            raise EntryptMisconfigurationExit()
        else:
            # Do not intercept if CLI was passed `-h`
            return super().__exit__(exc_type, exc_value, traceback)
