'''
                Regular expressions
'''

# Regular expressions are huge time-savers for programmers. 
# They allow you to specify a pattern of text to search for or filter. 
# All the regex functions in Python are in the re module.
import re

# Passing a string value representing your regular expression to re.compile() returns a Regex pattern object
# A Regex object’s search() method searches the string it is passed for any matches to the regex. 
# The search() method will return None if the regex pattern is not found in the string. 
# If the pattern is found, the search() method returns a Match object. 
# Match objects have a group() method that will return the actual matched text from the searched string.


# \d    -   Any character that is a numeric digit from 0 to 9.
# \D    -   Any character that is not a numeric digit from 0 to 9.
# \w    -   Any letter, numeric digit, or the underscore character.
# \W    -   Any character that is not a letter, numeric digit, or the underscore character.
# \s    -   Any space, tab, or newline character. (Think of this as matching /space/ characters.)
# \S    -   Any character that is not a space, tab, or newline.

# |     -   or
# *     -   match Zero or More
# +     -   match one or more
# ?     -   Optional
# ^     -   Not eg. [^aeiouAEIOU]

# [q-s] -  match character, number from q - s eg. [a-zA-Z0-9]

# {n}   -   match n times
# {n,m} -   match between n to m times
# {n,}  -   match n and more times
# {n,m}? -  non greedy matching i.e matches the shortest match
#

# ( ^ )  -  matching should occur at the beginning of the text eg. r'^Hello'
# ( $ )  -  matching should occur at the end of the text E.G r'\d$' -
# .     -   wildcard and will match any character except for a newline.
# (.*)  -   match anything E.g  r'First Name: (.*) Last Name: (.*)'
# ( .*? ) - Non greedy of above

# re.DOTALL as the second argument to re.compile() , you can make the dot character match
# all characters, including the newline character.
# re.IGNORECASE or re.I as a second argument to re.compile() to ignore case.
# re.VERBOSE as the second argument to re.compile() to match complicated text patterns with Verbose mode.
# Combining the arguments
# someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
# someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)


# search()  -   Search for the first instance
# findall() -   search for all matching instance
# The sub() -   Substituting Strings
# The sub() method for Regex objects is passed two arguments. The first argument is a string to replace any matches.
# The second is the string for the regular expression. The sub() method returns a string with the substitutions applied.

import re


def find_phone_num(text):
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    match = re.findall(pattern, text)
    return match


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
print(find_phone_num(message))


def find_batman_objects(text):
    pattern = re.compile(r'bat(man|mobile|rang|copter|bat)')
    return re.findall(pattern, text)


comic_text = 'I found batman working with batwoman fighting Gotham crime. ' \
             'Batman flew on batcopter will batwoman drove the batmobile. The both possessed a batrang.'
mo = find_batman_objects(comic_text)
print(mo)
