"""
            1 Data types 
"""

# This are category for values, and every value belongs to exactly one data type. 
# Most common data type in python are:


# 1.1 String - this is a text values. Always surround your string in quotes. For Example:
'Elkanah'
'Hello, I am learning Python'

# 1.2 Integer - this is any whole number, positive or negative. There is no limit to its size. For Example:
23
474774
0
-21

# 1.3 Float - is just any valid number that contains a decimal point. Again, there is no size limit. For Example:
33.341416
-575.6474562
0.425

# 1.4 Boolean - this is a data type that can be one of two values: either True or False. For Example:
True
False



'''
            2 Python Operators
'''


# Python offers many different operators for working with and comparing data types. For Example:

# 2.1 Arthmetic Operators - This operators are for doing arithmetic; 

#   **  -   Exponent
#   %   -   Reminder
#   //  -   Integer division/floored quotient ( 22 // 8 = 2)
#   /   -   Division (22/8 = 2.75)
#   *   -   Multiplication
#   +   -   Addition
#   -   -   Subtraction

j = 5
k = 2

z = j**k
print("ans1: ", z)
z = j*k
print("ans: ", z)
z = j % k
print("ans: ", z)
z = j//k
print("ans: ", z)
z = j/k
print("ans: ", z)
z = j+k
print("ans: ", z)
z = j-k
print("ans: ", z)

# 2.2 Comparison Operators - this compares two values and evaluate down to a single Boolean value. For Example:
# ==  Equal to
# !=  Not equal to
# <   Less than
# >   Greater than
# <=  Less than or equal to
# >=  Greater than or equal to

'hello' == 'hello' # True
'hello' == 'Hello' # False
'dog' != 'cat' # True
True == True # True
True != False # True
42 == 42.0 # True
42 == '42' # False
42 < 100 # True

# Text and Number Equivalence
# Although the string value of a number is considered a completely different
# value from the integer or floating-point version, an integer can be equal to a floating point.


# 2.3 Boolean Operators - this operators compare Boolean values.
# The three Boolean operators ( and , or , and not ) are used to compare Boolean values

# Expression        Evaluates to...
# True and True     True
# True and False    False
# False and True    False
# False and False   False
#
# True or True      True
# True or False     True
# False or True     True
# False or False    False
#
# not True          False
# not False         True

print("(4 < 5) and (5 < 6): ", (4 < 5) and (5 < 6))
print("(4 < 5) and (9 < 6): ", (4 < 5) and (9 < 6))
print("(1 == 2) or (2 == 2)", (1 == 2) or (2 == 2))



'''
            3 Variables and Keywords
'''
# a variable like a box in the computer’s memory where you can store a single value that can be accessed later.
# We create a variable by using variable name, an equal sign (assignment operator), and the value to be stored. 
# For Example: 
name = 'Elkanah Malonza'
username = "Alan"
unit_price = 49.99

# Rules of creating a variable
# 1. It can be only one word.
# 2. It can use only letters, numbers, and the underscore ( _ ) character.
# 3. It can’t begin with a number.
# 4. It cannot be a keyword
# keywords - have special meaning in the language

ALL_inbuilt_keywords = '''
        False, class, None, continue, True, def, and, del, as, elif, 
        assert, else, async, await, break, except, finally, 
        for, from, global, pass, raise, return, if, import, in, try, 
        is, while, lambda, with, nonlocal, yield, not, or,
'''



'''
            4 Inbuilt Function
'''
# Functions provide a way to compartmentalize your code into small tasks that can be called 
# from multiple places within an app. It also make you avoid duplicating code.

# Inbuilt Functions - this are function that are provided by python by default. Example:

print('I love Python')
name = input("Enter Your Name: ")
print(name)
len(name)

name = 'Malonza '
names = name * 3
print(names)
name = input("WHat is your Name: ")
print("You name is ", len(name), "Long")
print("THanks ", name, "for choosing Python3")

# str() , int() , and float() - TYpe Conversion
# int(7.7) => 7     float('7.7') => 7.7
dob = int(input("When were you born: "))
age = 2019 - dob
print("You are ", age, "years old")


# Formatting with f-strings
username = "Alan"
print(f"Hello {username}")
unit_price = 49.99
quantity = 30
print(f"Subtotal: ${quantity * unit_price}")

print(f"Subtotal: ${quantity * unit_price:,}")

print(f"Subtotal: ${quantity * unit_price:,.2f}")

# Formatting percent numbers
sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate}")
print(f"Sales Tax Rate {sales_tax_rate:.2%}")
print(f"Sales Tax Rate {sales_tax_rate:.1%}")
print(f"Sales Tax Rate {sales_tax_rate:.9%}")

# All built-in Function

abs(), aiter(), all(), any(), anext(), ascii(), bin(), bool(), breakpoint(), bytearray(), bytes(), 

callable(), chr(), classmethod(), compile(), complex() delattr(), dict(), dir(), divmod(), 

enumerate(), eval(), exec(), filter(), float(), format(), frozenset(), getattr(), globals(), 

hasattr(), hash(), help(), hex(), id(), input(), int(), isinstance(), issubclass(), iter(), 

len(), list(), locals(), map(), max(), memoryview(), min(), next(), object(), oct(), open(), ord(), 

pow(), print(), property(), range(), repr(), reversed(), round()

set(), setattr(), slice(), sorted(), staticmethod(), str(), sum(), super(), 

tuple(), type(), vars(), zip(), __import__()



"""
            5. Flow control statements
"""
# Flow control statements decides which Python instructions to execute under which conditions. 
# Flow control statements often start with a part called the condition, and 
# all are followed by a block of code called the clause. 
# Condition are Boolean expressions that when evaluates to true execute clause.

# 5.1 if...elif..else statements 

# An if statement’s clause will execute if the statement’s condition is True. 
# The clause is skipped if the condition is False. You may have a case where you want one of many possible clauses 
# to execute. The elif statement is an “else if” statement that always follows an if or another elif statement.
# if clause can optionally be followed by an else statement. 
# The else clause is executed only when the if statement’s and/or elif statement condition is False .

rate = int(input("1 to 10, how much would you rate me: "))
if rate >= 7:
    print("I offer Excellent Services, Thank you")
elif rate >= 6:
    print("I offer Good Services")
elif rate >= 5:
    print("I offer Fair Service")
elif rate >= 4:
    print("I need to improve quality my services")
elif rate >= 0:
    print("OH BOY, I should NOT be operating this business")

# 5.2 while Loop Statements
# The code in a while clause will be executed over and over, as long as the while statement’s condition is True.
x = 0
star = " "
while x < (rate/2):
    star = star + "* "
    x = x + 1
print("I offer", star, "Services")

# break Statements - They are used to break out program execution of a while loop’s clause early.
count = 0
while count < 5:
    print('Hello, world.')
    if count == 3:
        break
    count = count + 1


# continue statement - the program execution immediately jumps back to the start of the loop and reevaluates 
# the loop’s condition.
count = 0
while count < 5:
    count = count + 1
    if count == 3:
        continue
    print(count)

# for Loops and the range() Function
# used to execute a block of code only a certain number of times.
print("Using FOr loop to print 1 to 5")
for i in range(5):
    print(i)
print("Print 5 to 10")

for i in range(5, 11):
    print(i)
print("Printing in even numbers")

for i in range(0, 22, 2):
    print(i)
print("Printing multiples of 10 ")

for i in range(0, 102, 10):
    print(i)
print("Printing in reverse:- 10 to 0")

for i in range(10, -1, -1):
    print(i)
# ##
