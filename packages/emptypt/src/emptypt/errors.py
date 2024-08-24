from typing import Literal

__all__ = (
    "EntryptErrorCodes",
    "EntryptUserError",
    "EntryptMisconfigurationExit",
)

ERROR_DOCS_URL = "https://entrypt.readthedocs.io/en/latest/reference/"

EntryptErrorCodes = Literal["invalid-config"]


class EntryptErrorMixin:
    """A mixin class for common functionality shared by all Entrypt-specific errors.

    Attributes:
        message: A message describing the error.
        code: An optional error code from EntryptErrorCodes enum.
    """

    def __init__(self, message: str, *, code: EntryptErrorCodes | None) -> None:
        self.message = message
        self.code = code

    def __str__(self) -> str:
        if self.code is None:
            return self.message
        else:
            return f"{self.message}\n\nFor further information visit {ERROR_DOCS_URL}{self.code}"


class EntryptUserError(EntryptErrorMixin, TypeError):
    """An error raised due to incorrect use of Entrypt."""


class EntryptMisconfigurationExit(SystemExit):
    """
    An error raised due to incorrect Entrypt CLI configuration.

    Attributes:
        code: The exit code for the shell (always 1).
    """

    def __init__(self) -> None:
        self.code = 1
