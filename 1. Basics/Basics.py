# Maths Operations

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

# NUMBER FUNCTIONS
# abs(x) Returns the absolute value of number x (converts negative numbers to positive)
# bin(x) Returns a string representing the value of x converted to binary.
# float(x) Converts a string or number x to a the float data type
# format(x,y) Returns x formatted as directed by format string y.
# hex(x) Returns a string containing x converted to hexadecimal, prefixed with 0x.
# int(x) Converts x to the integer data type by truncating (not rounding) the decimal point and any digits after it.
# max(x,y,z ...) Takes any number of numeric arguments and returns whichever one is the largest.
# min(x,y,z ...) Takes any number of numeric arguments and returns whichever one is the smallest.
# oct(x) Converts x to an octal number, prefixed with 0o to indicate octal.
# round(x,y) Rounds the number x to y number of decimal places.
# type(x) Returns a string indicating the data type of x.



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

# Text and Number Equivalence
# Although the string value of a number is considered a completely different
# value from the integer or floating-point version, an integer can be equal to a floating point.
# 42 == '42'  >>> False
# 42 == 42.0  >>> True
# 42.0 == 0042.000  >>> True

# Boolean Values
spool = True
loops = False
print("My boolean Values are always two:", spool, "And", loops)

# == Equal to
# != Not equal to
# < Less than
# > Greater than
# <= Less than or equal to
# >= Greater than or equal to

print("10 == 10: ", 10 == 10)
print("11 == 10: ", 11 == 10)
print("10 > 10: ", 10 > 10)

# Boolean Operators
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

# Flow control statements
# if Statements
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
    print("OH BOY, I should operating this business")

# while Loop Statements
x = 0
star = " "
while x < (rate/2):
    star = star + "* "
    x = x + 1
print("I offer", star, "Services")

# for Loops and the range() Function
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
