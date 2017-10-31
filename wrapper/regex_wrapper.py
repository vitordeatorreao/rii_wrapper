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

    def parse_match(self, match, result_dir, key):
        """Parses the match result"""
        res = []
        if match is None:  # if there was no match for the regex in the query
            return ""
        if match is not None and not isinstance(match, str) and not match.groups():
            return key
        elif isinstance(match, str):
            return match
        for group in match.groups():
            if group is None:
                break
            res += [group]
        return " ".join(res)

    def fill_template(self, query_str):
        """Fills the template given in self.template"""
        result = dict()
        for key in self.template:
            if key == "Optionals":
                matches = re.findall(self.template[key], query_str, re.I)
                ms = []
                for match in matches:
                    m = self.parse_match(match, result, key)
                    ms.append(m)
                if len(ms) > 0:
                    result["Optionals"] = ", ".join(ms)
                else:
                    result["Optionals"] = ""
                continue
            match = re.search(self.template[key], query_str, re.I)
            result[key] = self.parse_match(match, result, key)
        if len(result["Complete"]) > 0:
            optionals = ["completo"]
            if len(result["Optionals"]) > 0:
                optionals += [result["Optionals"]]
            result['Optionals'] = ", ".join(optionals)
        if len(result["Complete"]) > 0:
            result['Air-Conditioning'] = "sim"
        del result['Complete']

        return result
