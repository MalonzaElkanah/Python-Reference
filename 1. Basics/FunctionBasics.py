'''
            Functions
'''
# Functions provide a way to compartmentalize your code into small tasks that can be called from multiple places 
# within an app. It also make you avoid duplicating code.

'''
Inbuilt Functions - this are function that are provided by python by default. Example:

'''

print('I love Python')
name = input("Enter Your Name: ")
print(name)
len(name)

'''
defining a function - You can also define your own functions
'''
def intro():
    print("Hello Stranger.")
    print("I love Python.")

intro()

'''
Function with arguments 
You can also define your own functions that accept arguments anonymous functions, 
'''
def add(x,y):
    z = x + y
    print(z)

add(3,8) # 11

'''
Return Values and return Statements
function call evaluates to is called the return value of the function
'''
def add(x,y):
    return x + y

add(2,3) # 5

'''
Defining optional parameters with defaults
'''
def add(x=0,y=0):
    return x + y

add() # 0
add(4) # 4
add(2,3) # 5

'''
Using keyword arguments (kwargs)
If you like, you can tell the function which parameter will have what value by using the syntax 
parameter = value in the code that’s calling the function.
'''
def divide(x,y):
    return x/y

divide(y=2, x=3) # 1.5
divide(x=2, y=3) # 0.6666666666666666

'''
Passing in an arbitrary number of arguments
You can also design the function so that it accepts any number of arguments, use *args as the parameter name*
Whatever you pass in becomes a tuple named args inside the function. 
A tuple isan immutable list (a list you can’t change).
'''
def sorter(*args):
    """ Pass in any number of arguments separated by commas
    Inside the function, they treated as a tuple named args """
    # The passed-in
    # Create a list from the passed-in tuple
    newlist = list(args)
    # Sort and show the list.
    newlist.sort()
    return newlist

sorter(2, 0.42, -42,4.24, 25, 5)

'''
Anonymous Functions/lambda functions. 
The anonymous because function doesn’t need to have a name.
'''
# Syntax: Lambda arguments : expression
name = lambda anystring : anystring.lower()
percent = lambda n : f"{n:.2%}"
print(percent(.6)) # 60.00%

'''
DECORATORS
'''

# A NUMBER GUESING EXAMPLE:
from random import randint


def numbertoguess():
    return randint(1, 20)


def guess():
    return int(input())


def checknumber(number, input_num):
    if number > input_num:
        print("The Number is too low")
        return False
    elif number < input_num:
        print("The Number is too high")
        return False
    else:
        print("Correct Number")
        return True


print("Guess a Number between 1 and 20: ")
num = numbertoguess()
for i in range(1, 7):
    num2 = guess()
    if checknumber(num, num2):
        print("Congratulations!")
        break
