"""A simple math operations package."""

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0.0.0+unknown"

from .operations import add, multiply

__all__ = ["add", "multiply", "__version__"]
