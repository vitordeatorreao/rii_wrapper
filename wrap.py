"""Per query wrapper"""

import fileinput

from wrapper import RegexWrapper
from wrapper import remove_diacritics

from exercise_wrap import TEMPLATE, exercise_output

def main():
    """Main function"""
    wrapper = RegexWrapper(TEMPLATE)
    for line in fileinput.input():
        input_ = remove_diacritics(line)
        template = wrapper.fill_template(input_)
        print(exercise_output(template))

if __name__ == "__main__":
    main()
