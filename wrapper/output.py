"""Contains a few functions for formatting the filled templates"""

def as_unordered_list(filled_template):
    """Formats the filled template as an unordered list"""
    if not isinstance(filled_template, dict):
        raise ValueError("A filled template is a dictionary, not {0}".format(
            type(filled_template)
        ))
    result = ""
    for key in filled_template:
        if not isinstance(key, str):
            raise ValueError("A filled template's keys must be str, not {0}"
                             .format(type(key)))
        value = filled_template[key]
        if not isinstance(value, str):
            raise ValueError("A filled template's value must be str, not {0}"
                             .format(type(value)))
        result += "{0}: {1}\n".format(key, value)
    return value
