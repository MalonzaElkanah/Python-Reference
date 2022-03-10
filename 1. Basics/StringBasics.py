# String Basics

# In python, You can do more with strings other than write, print, and access strings. 
# You can extract partial strings from string values, add or remove spacing, convert letters to lowercase 
# or uppercase, check that strings are formatted correctly, etc. 
# This is easily done by use of different string method, indexes and slices and other in-built functions. 


'''
				Working with strings using indexes and slices
'''
s = "Hello World, I love Programming with Python."
# s[i:j:k] A slice of s from i to j with step k .
s[0:40:2] # 'HloWrd  oePormigwt y'


'''
				Working with strings using in-built functions
'''
s = 'World-war:z'
# min(s) The smallest (lowest) item of string s .  uses Ascii - space smaller than a-z,A-Z
min(s) # '-'
# max(s) The largest (highest) item of string s .
max(s) # 'z'


'''
				Working with strings using string methods and attributes
'''

# Examples of string methods and attributes. 
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

# s.count(x) The total number of times string x appears in larger string s .

# s.capitalize() Returns a string with the first letter capitalized, the rest lowercase.
# s.count(x,[y.z]) Returns the number of times string x appears in string s . Optionally you can add y as
# a starting point and z as an ending point to search only a portion of the string.
# s.find(x,[y.z]) Returns a number indicating the first position at which string x can be found in string
# s . Optional y and z parameters allow you to limit the search to a portion of the
# string. Returns –1 if none found.
# s.index(x,[y.z]) Similar to find but returns a “substring not found” error if string x can’t be found
# in string y .
# s.index(x[, i[, j]]) The numeric position of the first occurrence of x in string s . The optional i and
# j let you limit the search to the characters from i to j .
# s.isalpha() Returns True if s is at least one character long and contains only letters (A-Z or a-z).
# s.isdecimal() Returns True if s is at least one character long and contains only numeric
# characters (0-9).
# s.islower() Returns True if s contains letters and all those letters are lowercase.
# s.isnumeric() Returns True if s is at least one character long and contains only numeric
# characters (0-9).
# s.isprintable() Returns True if string s contains only printable characters.
# s.istitle() Returns True if string s contains letters and the first letter of each word is uppercase
# followed by lowercase letters.
# s.isupper() Returns True if all letters in the string are uppercase.
# s.lower() Returns s with all letters converted to lowercase.
# s.lstrip() Returns s with any leading spaces removed.
# s.replace(x,y) Returns a copy of string s with all characters x replaced by character y .
# s.rfind(x,[y,z]) Similar to find but searches backwards from the start of the string. If y and z are
# provided, searches backwards from position z to position y . Returns –1 if string x
# not found.
# s.rindex() Same as . rfind but returns an error if the substring isn’t found.
# s.rstrip() Returns string x with any trailing spaces removed.
# s.strip() Returns string x with leading and trailing spaces removed.
# s.swapcase() Returns string s with uppercase letters converted to lowercase and lowercase letters
# converted to uppercase.
# s.title() Returns string s with the first letter of every word capitalized and all other letters
# lowercase.
# s.upper() Returns string s with all letters converted to uppercase.
