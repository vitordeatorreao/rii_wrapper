"""Basic regular expression wrapper"""

import re

class RegexWrapper(object):
    """A regular expression-based wrapper for extracting information"""

    def __init__(self, template):
        """RegexWrapper's constructor

        Parameters
        ----------
        template : dict
            A dictionary with field name -> field regex

        Examples
        --------
        >>> wrapper = RegexWrapper({ "complete": r"comp\w+" })
        """
        if not isinstance(template, dict):
            raise ValueError("The 'template' parameter must be a dictionary")
        self.template = template

    def fill_template(self, query_str):
        """Fills the template given in self.template"""
        result = dict()
        for key in self.template:
            match = re.search(self.template[key], query_str, re.I)
            res = []
            if match is None: # if there was no match for the regex in the query
                result[key] = ""
                continue
            if match is not None and not match.groups():
                result[key] = key
                continue
            for group in match.groups():
                if group is None:
                    break
                res += [group]
            result[key] = " ".join(res)
        return result
