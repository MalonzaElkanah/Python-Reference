'''
            Importing libraries
'''

# Python comes with a set of modules called the standard library 
# - which a Python program that contains a related group of functions that can be embedded in your programs. 
# Before you can use the functions in a module, you must import the module with an import statement.

# Example: the random module has random number–related functions,

import random

for i in range(15):
    print(random.randint(1, 10))


# Example: the math module has mathematics related functions
import math
print(math.sqrt(81))


# EXAMPLE: 
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')


# There may be times where you don’t really need the whole kit-and-caboodle. 
# In those cases, you can import just what you need using a syntax like this:
from math import pi

print(pi) # 3.141592653589793

from math import pi, sqrt



