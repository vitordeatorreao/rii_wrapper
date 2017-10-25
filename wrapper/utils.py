"""Utility functions"""

from unidecode import unidecode

def remove_diacritics(string):
    """Removes diacritics from the given string

    Parameters
    ----------
    string : str
        The string from which diacritics should be removed

    Returns
    -------
    string : str
        The string with its diacritics removed
    """
    uni = unidecode(string)
    # r = uni.encode("ascii")
    return uni
