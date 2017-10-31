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

    def parse_match(self, match, key, substring):
        """Parses the match result"""
        res = []
        if match is None:  # if there was no match for the regex in the query
            return "", substring
        if match is not None and not isinstance(match, str) and not match.groups():
            substring = substring[:match.start()] + substring[match.end():]
            return key, substring
        elif isinstance(match, str):
            substring = substring.replace(match, "")
            return match, substring
        for group in match.groups():
            if group is None:
                break
            res += [group]
        substring = substring[:match.start()] + substring[match.end():]
        return " ".join(res), substring

    def fill_template(self, query_str):
        """Fills the template given in self.template"""
        result = dict()
        substring = query_str
        for key in self.template:
            if key == "Optionals":
                continue
            match = re.search(self.template[key], substring, re.I)
            result[key], substring = self.parse_match(match, key, substring)
        remaining_words = []
        for word in substring.split(","):
            clean_word = word.strip().lower().replace(",", "").replace(".", "")
            if len(clean_word) < 1:
                continue
            remaining_words.append(clean_word)
        result["Optionals"] = ", ".join(remaining_words)
        if len(result["Complete"]) > 0:
            optionals = ["completo"]
            if len(result["Optionals"]) > 0:
                optionals += [result["Optionals"]]
            result['Optionals'] = ", ".join(optionals)
        if len(result["Complete"]) > 0:
            result['Air-Conditioning'] = "sim"
        del result['Complete']

        return result
