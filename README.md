# Python-Reference

In the recent years python has become one of the most popular programming language. This is mainly because its easy to learn and use, Everything you need to learn (and do) Python is free, its wide application for instance Web Development, Scientific Computing, Scripting, and more.
In this article we will discuss the right way to learn python. After learning python basics and intermediate python, learning python may vary according to the area of application. This article is ment to guide you through the journey of learning python depending on your area of application. We will takes you on a tour through some really cool libraries and technologies. But first, lets look at the various application of python. 

## Application of Python
1. Big Data and data science,
2. artificial intelligence, machine learning and neural networks, 
3. physical computing (Raspberry Pi computer)
4. Web Development
5. Scripts and Automation


## Python Basics 
Before you can do anything, we have to learn some basic python programming concepts.
The basic topics you need master as python biginner are:
* Data types - Numbers, Strings, Boolean, 
* Python Operators - Arthmetic Operators, Comparison Operators, Boolean Operators
* Variables and Keywords
* Flow Control Statements - if statements, while loops, for loops
* Function - Inbuilt Functions, defining a function, parameters, anonymous functions,  
* Python Data Types - Lists, Tuples, Sets, Dictionaries
* Classes and Objects, Inheritance, 
* Debugging, Handling the error and exceptions - try..except..else..finally
* importing libraries
* String In-depth
* Number in-depth
* Date and time

### 1.1 Data types 
This are category for values, and every value belongs to exactly one data type. Most common data type in python are:

String - this is a text values. Always surround your string in quotes. For Example:
'Elkanah'
'Hello, I am learning Python'

Integer - this is any whole number, positive or negative. There is no limit to its size. For Example:
23
474774
0
-21

Float - is just any valid number that contains a decimal point. Again, there is no size limit. For Example:
33.341416
-575.6474562
0.425

Boolean - this is a data type that can be one of two values: either True or False. For Example:
True
False

### 1.2 Python Operators 
Python offers many different operators for working with and comparing data types. For Example:
Arthmetic Operators - This operators are for doing arithmetic; addition, subtraction, multiplication, division, and others.
** 	Exponent 
% 	Modulus/remainder 
// 	Integer division/floored quotient 
/ 	Division 
* 	Multiplication 
- 	Subtraction 
+ 	Addition
2 ** 3 # 8
22 % 8 # 6
22 // 8 # 2
22 / 8 # 2.75
3 * 5 # 15
5 - 2 # 3
5 + 2 # 5

Comparison Operators - this compares two values and evaluate down to a single Boolean value. For Example:
== 	Equal to
!= 	Not equal to
< 	Less than
> 	Greater than
<= 	Less than or equal to
>= 	Greater than or equal to

'hello' == 'hello' # True
'hello' == 'Hello' # False
'dog' != 'cat' # True
True == True # True
True != False # True
42 == 42.0 # True
42 == '42' # False
42 < 100 # True

Boolean Operators - this operators compare Boolean values.
and - binary operator(always take two Boolean values) that evaluates an expression to True if both Boolean values are True, otherwise, it evaluates to False. For Example:  
True and True  	# True
True and False 	# False
False and True 	# False
False and False # False

or - binary operator that evaluates an expression to True if either of the two Boolean values is True . If both are False , it evaluates to False. For Example:
True or True 	# True
True or False 	# True
False or True 	# True
False or False 	# False

not - evaluates to the opposite Boolean value. For Example:
not True 	# False
not False	# True

### 1.3 Variables
a variable like a box in the computer’s memory where you can store a single value that can be accessed later.
We create a variable by using variable name, an equal sign (assignment operator), and the value to be stored. For Example: 
name = 'Elkanah Malonza'

Rules of creating a variable
1. It can be only one word.
2. It can use only letters, numbers, and the underscore ( _ ) character.
3. It can’t begin with a number.
4. It cannot be a keyword
keywords - have special meaning in the language

### 1.4 Flow Control Statements 
Flow control statements decides which Python instructions to execute under which conditions. Flow control statements often start with a part called the condition, and all are followed by a block of code called the clause. Condition are Boolean expressions that when evaluates to true execute clause.

if...elif..else statements 
An if statement’s clause will execute if the statement’s condition is True. The clause is skipped if the condition is False.
You may have a case where you want one of many possible clauses to execute. The elif statement
is an “else if” statement that always follows an if or another elif statement.
if clause can optionally be followed by an else statement. The else clause is executed only when the if statement’s and/or elif statement condition is False .
Example
if name == 'Elkanah':
	print('Hello Elkanah')
elif name == 'Malone':
	print('Hello Malone')
else:
	print('Hello')

if password == 'swordfish':
	print('Access granted.')
else:
	print('Wrong password.')


while loops
The code in a while clause will be executed over and over, as long as the while statement’s condition is True.
For Example:
count = 0
while count < 5:
	print('Hello, world.')
	count = count + 1
break Statements - They are used to break out program execution of a while loop’s clause early.
count = 0
while count < 5:
	print('Hello, world.')
	if count == 3:
		break
	count = count + 1
continue statement - the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition.
count = 0
while count < 5:
	count = count + 1
	if count == 3:
		continue
	print(count)

for loops and the range() Function
used to execute a block of code only a certain number of times.
for i in range(10):
	print('Malone Ten Times')


### 1.5 Function
Functions provide a way to compartmentalize your code into small tasks that can be called from multiple places within an app. It also make you avoid duplicating code.

Inbuilt Functions - this are function that are provided by python by default. Example:
print('I love Python')
name = input("Enter Your Name: ")
print(name)
len(name)

defining a function 
You can also define your own functions
def intro():
	print("Hello Stranger.")
	print("I love Python.")

intro()

Function with arguments 
You can also define your own functions that accept arguments anonymous functions, 
def add(x,y):
	z = x + y
	print(z)

add(3,8) # 11

Return Values and return Statements
function call evaluates to is called the return value of the function
def add(x,y):
	return x + y

add(2,3) # 5

Defining optional parameters with defaults
def add(x=0,y=0):
	return x + y

add() # 0
add(4) # 4
add(2,3) # 5

Using keyword arguments (kwargs)
If you like, you can tell the function which parameter will have what value by using the syntax parameter = value in the code that’s calling the function.
def divide(x,y):
	return x/y

divide(y=2, x=3) # 1.5
divide(x=2, y=3) # 0.6666666666666666

Passing in an arbitrary number of arguments
You can also design the function so that it accepts any number of arguments, use *args as the parameter name*
Whatever you pass in becomes a tuple named args inside the function. A tuple isan immutable list (a list you can’t change).

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

Anonymous Functions/lambda functions. 
The anonymous because function doesn’t need to have a name.
Syntax: Lambda arguments : expression
name = lambda anystring : anystring.lower()
percent = lambda n : f"{n:.2%}"
print(percent(.6)) # 60.00%

### 1.6 Python Data Structures - 
Lists
A list is a value that contains multiple values in an ordered sequence. A list begins with an opening square bracket and ends with a closing square bracket, []. Values inside the list are also called items which are separated with commas. Example:
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

To get individual values in a List we use Indexes. Example:
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
print(subjects[0]) # Maths 
print(subjects[0]) # Physics 

list methods
append()    - Adds an item to the end of the list.
clear()     - Removes all items from the list, leaving it empty.
copy()      - Makes a copy of a list.
count()     - Counts how many times an element appears in a list.
extend()    - Appends the items from one list to the end of another list.
index()     - Returns the index number (position) of an element within a list.
insert()    - Inserts an item into the list at a specific position.
pop()       - Removes an element from the list, and provides a copy of that item 
                that you can store in a variable.
remove()    - Removes one item from the list.
reverse()   - Reverses the order of items in the list.
sort()      - Sorts the list in ascending order. 
                Put reverse=True inside the parentheses to sort in descending order.

Tuples
A tuple is just an immutable list. In other words, a tuple is a list, 
but after it’s defined you can’t change it. 
Tuples are typed with parentheses, ( and ) , instead of square brackets, [ and ].
'''
subjects = ('History', 'Geography', 'Biology', 'Physics', 'Maths')
num = (5, 7, 8, 5, 3, 8, 5, 2, 1, 8, 5, 7)

List methods and techniques that modified list data won't work with tuple but the rest will


Sets
Python Sets is also a means of organizing data. The difference between a set and a list is that the items in set have no specific order. Even though you may define the set with the items in a certain order, 
none of the items get index numbers to identify their positions.

To define a set, use curly braces where you would have used square brackets 
for a list and parentheses for a tuple. For example:

subjects = {'Maths', 'Physics', 'Biology', 'Geography', 'History'}
num = {5, 7, 8, 5, 3, 8, 5, 2, 1, 8, 5, 7}

You can’t change the order of items in a set, so you cannot use .sort() to sort the set or .reverse() to reverse its order. 


Dictionaries
Like a list, a dictionary is a collection of many values, but unlike indexes for lists, indexes 
for dictionaries can use many different data types, not just integers. 
Indexes for dictionaries are called keys, and a key with its associated value is called a key-value pair.
In code, a dictionary is typed with braces, {}. Example:

person = {
    "name": "Elkanah",
    "gender": "Male",
    "height": "5.9 Foot",
    "weight": "67 kg",
}

You can access these values through their keys:
print(person["name"]) # Elkanah
print(person["height"]) # 5.9 Foot

    clear()     - Empties the dictionary by remove all keys and values.
    copy()      - Returns a copy of the dictionary.
    fromkeys()  - Returns a new copy of the dictionary but with only specified keys and values.
    get()       -  Returns the value of the specified key, or None if it doesn’t exist.
    items()     -  Returns a list of items as a tuple for each key-value pair.
    keys()      - Returns a list of all the keys in a dictionary.
    pop()       - Removes the item specified by the key from the dictionary, and stores it in a variable.
    popitem()   - Removes the last key-value pair.

    setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, 
                    with the specified value.
    update()    - Updates the value of an existing key, 
                    or adds a new key-value pair if the specified key isn’t already in the dictionary.
    values()    - Returns a list of all the values in the dictionary.


### 1.7 Classes and Objects, Inheritance, 
like functions classes also allow you to compartmentalize code and data. object stems from the fact that
the model resembles objects in the real word in that each object is a thing that has certain attributes and characteristics that make it unique.

Class: A piece of code from which you can generate a unique object, where each object is a single instance of the class. Think of it as a blueprint or factory from which you can create individual objects.
Instance: One unit of data plus code generated from a class as an instance of that class. Each instance of a class is also called an object created by class.
Attribute: A characteristic of an object that contains information about the object. Also called a property of the object. An attribute name is preceded by dot, as in member.username which may contain the username for one site member.
Method: A Python function that’s associated with the class. It defines an action that object can perform. In an object, you call a method by preceding the method name with a dot, and following it with a pair of parentheses. For example member.archive() may be a method that archives (deactivates) the member’s account.

class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def display_name(self):
        print(self.name)

    def display_age(self):
        print(self.age)


puppy = Dog(3, 'TOM')
puppy.display_age()
puppy.display_name()
puppy.change_name("Cindy")
puppy.display_name()


Inheritance
inheritance is by creating sub-classes within a class. The class defines things that apply to all instances of that class. Each subclass defines things that are relevant only to the subclass without
replacing anything that’s coming from the generic “parent” class.

Syntax:

class parent:
   statements
class child(parent):
   statements

Subclasses inherit all the attributes and methods of some higher-level main class, or parent class, which is usually referred to as the base class.

class Quadrilateral:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        p = self.a + self.b + self.c + self.d
        print("perimeter: ", p)


q1 = Quadrilateral(4, 5, 7, 9)
q1.perimeter()


class Rectangle(Quadrilateral):
    def __init__(self, a, b):
        super(Rectangle, self).__init__(a, b, b, a)

    def area(self):
        area = self.a * self.b
        print("Area:", area)


r1 = Rectangle(20, 10)
r1.perimeter()
r1.area()


### 1.8 Debugging, Handling the error and exceptions - try..except..else..finally


### 1.9 importing libraries
import random
import os, sys, math

for i in range(15):
    print(random.randint(1, 10))

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')



### 1.10 String In-depth
# s[i:j:k] A slice of s from i to j with step k .
# min(s) The smallest (lowest) item of string s .  uses Ascii - space smaller than a-z,A-Z
# max(s) The largest (highest) item of string s .
# s.index(x[, i[, j]]) The numeric position of the first occurrence of x in string s . The optional i and
# j let you limit the search to the characters from i to j .
# s.count(x) The total number of times string x appears in larger string s .

# s.capitalize() Returns a string with the first letter capitalized, the rest lowercase.
# s.count(x,[y.z]) Returns the number of times string x appears in string s . Optionally you can add y as
# a starting point and z as an ending point to search only a portion of the string.
# s.find(x,[y.z]) Returns a number indicating the first position at which string x can be found in string
# s . Optional y and z parameters allow you to limit the search to a portion of the
# string. Returns –1 if none found.
# s.index(x,[y.z]) Similar to find but returns a “substring not found” error if string x can’t be found
# in string y .
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






### 1.11 Number in-depth
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


# import Math
# math.sqrt(x)      -
# math.acos(x) Returns the arc cosine of x in radians.
# math.atan(x) Returns the arc tangent of x, in radians.
# math.atan2(y, x) Returns atan(y / x), in radians.
# math.ceil(x) Returns the ceiling of x, the smallest integer greater than or equal to x.
# math.cos(x) Returns the cosine of x radians.
# math.degrees(x) Converts angle x from radians to degrees.
# math.e Returns the mathematical constant e (2.718281 . . .)
# math.exp(x) Returns e raised to the power x, where e is the base of natural logarithms.
# math.factorial(x) Returns the factorial of x.
# math.floor() Returns the floor of x, the largest integer less than or equal to x.
# math.isnan(x) Returns True if x is not a number, otherwise returns False.
# math.log(x,y) Returns the natural logarithm of x to base y.
# math.log2(x) Returns the base-2 logarithm of x.
# math.pi Returns the mathematical constant pi (3.141592 . . .).
# math.pow(x, y) Returns x raised to the power y.
# math.radians(x) Converts angle x from degrees to radians.
# math.sin(x) Returns the arc sine of x, in radians.
# math.sqrt(x) Takes any number of numeric arguments and returns whichever one is the smallest.
# math.tan(x) Returns the tangent of x radians.
# math.tau() Returns the mathematical constant tau (6.283185 . . .).


### 1.12 Date and time
# Import the datetime module, nickname dt
import datetime as dt
# Store today's date in a variable named today.
today = dt.date.today()
# Store some other date in a variable called last_of_teens
last_of_teens = dt.date(2019, 12, 31)
print(last_of_teens.month)
print(last_of_teens.day)
print(last_of_teens.year)
# Formatting Strings for Dates and Times

# %a Weekday, abbreviated Sun
# %A Weekday, full Sunday
# %w Weekday number 0-6, where 0 is Sunday 0
# %d Number day of the month 01-31 31
# %b Month name abbreviated Jan
# %B Month name full January
# %m Month number 01-12 01
# %y Year without century 19
# %Y Year with century 2019
# %H Hour 00-23 23
# %I Hour 00-12 11
# %p AM/PM PM
# %M Minute 00-59 01
# %S Second 00-59 01
# %f Microsecond 000000-999999 495846
# %z UTC offset -0500
# %Z Time zone EST
# %j Day number of year 001-366 300
# %U Week number of year, Sunday as the first day of week, 00-53 50
# %W Week number of year, Monday as the first day of week, 00-53 50
# %c Local version of date and time Tue Dec 31
# 23:59:59 2018
# %x Local version of date 12/31/18
# %X Local version of time 23:59:59
# %% A % character %

print(f"{last_of_teens:%A, %B %d, %Y}")
today_s_date = f"{today:%m/%d/%Y}"
print(today_s_date)
new_years_day = dt.date(2019, 1, 1)
memorial_day = dt.date(2019, 5, 27)
days_between = memorial_day - new_years_day


## Intermediate Python 
* Regular Expressions
* File Operations
* Working with web
*
* 
****
* Making your own module/library

## Scripts and Automation
* Web Scrapping - Selium
* Time, Schduling Tasks and Lauching Programs
* Creating and manupulating PDFs, Word Doc, Excel, CSV Files
* Networking Protocals
* Sending Email and Text
* Manipulating Images
* Controlling Keyboard and Mouse
*

## Web Development
* Web
* Flask Web Framework
* Django Web FRamework
* Fast APIs
***

## Data Science
* Numpy
* Pandas
* MatPlotLib
* 
*
*

## Machine Learning and AI
* Tensor Flow
* NumPy
* 
***

## Physical Computing
* 
* 
****


