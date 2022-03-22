# If no other arguments are passed other than the string to strip,
# then whitespace characters will be removed from the beginning and end of the string.
# Otherwise, the characters specified in the second argument to the function will be removed from the string.

import re


def remove(string, char_to_removed=' '):
    raw = r''+char_to_removed+r'+'
    pattern = re.compile(raw)
    return pattern.sub('', string)


my_data = "Regular expressions can not only find text patterns " \
          "but can also substitute new text in place of those patterns. " \
          "The sub() method for Regex objects is passed two arguments. " \
          "The first argument is a string to replace any matches. " \
          "The second is the string for the regular expression. " \
          "The sub() method returns a string with the substitutions applied."

print(remove(my_data))
print(remove(my_data, "a"))
