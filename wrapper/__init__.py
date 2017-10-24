"""Inteligent Information Recovery Wrapper extractor"""

from .output import as_unordered_list
from .regex_wrapper import RegexWrapper
from .utils import remove_diacritics

__all__ = [
    "as_unordered_list",
    "RegexWrapper",
    "remove_diacritics",
]
