'''The basic Python data structures in Python include:

    Lists
    Sets
    Tuples
'''

''' 
###########################################################################################
######################################## 1. Lists #########################################
###########################################################################################

A list is a value that contains multiple values in an ordered sequence. 
A list begins with an opening square bracket and ends with a closing square bracket, [] . 
Values inside the list are also called items which are separated with commas. Example:
'''
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#To get individual values in a List we use Indexes. Example:
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
print(subjects[0]) # Maths 
print(subjects[0]) # Physics 

# Lists can also contain other list values.
food = [['tea', 'coffee', 'water'], ['beef', 'pork', 'mutton', 'fish', 'chicken'], ['rice', 'pasta']]
beverage = food[0]
print(beverage) # ['tea', 'coffee', 'water']
print(food[1][3]) # 'fish'


# negative indexes - The integer value -1 refers to the last index in a list, 
# the value -2 refers to the second-to-last index in a list, and so on. Example:
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(num[-1]) # 0
print(num[-2]) # 9
print(num[-5]) # 6


# A slice can get several values from a list, in the form of a new list.
# The first integer in a slice is the index where the slice starts. 
# The second integer is the index where the slice ends but will not include it.
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
print(subjects[1:4]) # ['Physics', 'Biology', 'Geography']


# Leaving out the first index is the same as using 0 , or the beginning of the list. 
# Leaving out the second index is the same as using the length of the list, 
# which will slice to the end of the list.
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
print(subjects[:3]) # ['Maths', 'Physics', 'Biology']
print(subjects[3:]) # ['Geography', 'History']


# Changing Values in a List with Indexes
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
subject[0] = 'Mathematics'
print(subject) # ['Mathematics', 'Physics', 'Biology', 'Geography', 'History']


# Adding two lists using + operator
core_subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
supplementary_subjects = ['Programming', 'Sports', 'Communication']
subjects = core_subjects + supplementary_subjects
print(subjects)  
# ['Maths', 'Physics', 'Biology', 'Geography', 'History', 'Programming', 'Sports', 'Communication']


# Replicating a list using * operator
num = [1, 3, 5]
print(num*3) # [1, 3, 5, 1, 3, 5, 1, 3, 5]


# Removing Values from Lists with del Statements
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
del subjects[2]
print(subjects) # ['Maths', 'Physics', 'Geography', 'History']


# Using for Loops with Lists
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
for sub in subjects:
    print(sub)


# The in and not in Operators
# You can determine whether a value is or isn’t in a list with the in and not in operators.
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
print('Physics' in subjects) # True
print('Physics' not in subjects) # False
print('Programming' in subjects) # False
print('Programming' not in subjects) # True


# Getting a List’s Length with len()
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
print(len(subjects))


# Multiple Assignment using Lists
# You can assign multiple variables with the values in a list in one line of code.
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
maths, physics, bio, geo, history = subjects


# Converting Types with the list() Functions
line1 = 'hello'
line1_list = list(line1)
print(line1_list) # ['h', 'e', 'l', 'l', 'o']
subjects = ('History', 'Geography', 'Biology', 'Physics', 'Maths')
subjects = list(subjects) # ['History', 'Geography', 'Biology', 'Physics', 'Maths']



#  List Methods
list_methods = """

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
"""

# index()
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
print(subject.index('Physics')) # 1


# append()
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
subject.append('Programming') 
print(subject) # ['Maths', 'Physics', 'Biology', 'Geography', 'History', 'Programming']


# insert()
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
subject.insert('Programming', 1) 
print(subject) # ['Maths', 'Programming', 'Physics', 'Biology', 'Geography', 'History']


# remove()
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
subject.remove('Biology') 
print(subject) # ['Maths', 'Physics', 'Geography', 'History']
# NOTE: If the value appears multiple times in the list, only the first instance of the value will be removed.


# sort()
# Arrange in alphabetical order
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
subjects.sort() 
print(subjects) # ['Biology', 'Geography', 'History', 'Maths', 'Physics' ]

# Arrange in numeric order
random_num = [5, 5, 3, 8, 2, 1, 8, 0, 7]
random_num.sort() # [0, 1, 2, 3, 5, 5, 7, 8, 8]

# You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order.
random_num = [5, 5, 3, 8, 2, 1, 8, 0, 7]
random_num.sort(reverse=True) # [8, 8, 7, 5, 5, 3, 2, 1, 0]

# you cannot sort lists that have both number values and string values in them, 
# sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings. 
# This means uppercase letters come before lower-case letters.
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort() # ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

# you need to sort the values in regular alphabetical order, 
# pass str.lower for the key keyword argument in the sort() method call.
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower) # ['a', 'A', 'z', 'Z']



# pop()
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
# remove last subject
last_subject = subjects.pop()
print(subjects) # ['Maths', 'Physics', 'Biology', 'Geography']
print(last_subject) # 'History'

# remove first subject
first_subject = subjects.pop(0)
print(subjects) # ['Physics', 'Biology', 'Geography']
print(first_subject) # 'Maths' 



# count()
num = [5, 7, 8, 5, 3, 8, 5, 2, 1, 8, 5, 7]
num_count = num.count(5)
print(num_count) # 4


# extend()
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
supplementary_subjects = ['Programming', 'Sports', 'Communication']
subjects.extend(supplementary_subjects)
print(subjects) # ['Maths', 'Physics', 'Biology', 'Geography', 'History', 'Programming', 'Sports', 'Communication']


# clear()
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
subjects.clear()
print(subjects) # [ ]


# reverse()
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
subjects.reverse()
print(subjects) # ['History', 'Geography', 'Biology', 'Physics', 'Maths']


# copy()
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
subject_copy = subjects.copy()
print(subject_copy) # ['Maths', 'Physics', 'Biology', 'Geography', 'History']



'''
###########################################################################################
######################################## 2. Tuple #########################################
########################################################################################### 

A tuple is just an immutable list. In other words, a tuple is a list, 
but after it’s defined you can’t change it. 
Tuples are typed with parentheses, ( and ) , instead of square brackets, [ and ].
'''
subjects = ('History', 'Geography', 'Biology', 'Physics', 'Maths')
num = (5, 7, 8, 5, 3, 8, 5, 2, 1, 8, 5, 7)

# List methods and techniques that modified list data won't work with tuple but the rest will:
print(num.count(5)) # 4
print(type(subjects)) # <class 'tuple'>
print(len(num)) # 12
print('Physics' in subjects) # True

# Converting to Tuple Types with tuple() Functions
subjects = ['Maths', 'Physics', 'Biology', 'Geography', 'History']
subjects = tuple(subjects)
print(subjects) # ('Maths', 'Physics', 'Biology', 'Geography', 'History')



'''
###########################################################################################
######################################## 3. Sets  #########################################
########################################################################################### 

Python Sets is also a means of organizing data. The difference between a set and a list is that 
the items in set have no specific order. 
Even though you may define the set with the items in a certain order, 
none of the items get index numbers to identify their positions.

To define a set, use curly braces where you would have used square brackets 
for a list and parentheses for a tuple. For example:
'''
subjects = {'Maths', 'Physics', 'Biology', 'Geography', 'History'}
num = {5, 7, 8, 5, 3, 8, 5, 2, 1, 8, 5, 7}


# You can’t change the order of items in a set, so you cannot use .sort() to sort the set or 
# .reverse() to reverse its order. 
# You can use len() to determine size of set and in operator to check if an item exists.


# add() - You can add a single new item to a set
subjects = {'Maths', 'Physics', 'Biology', 'Geography', 'History'}
subjects.add('Programming')
print(subjects) # {'Maths', 'Physics', 'Biology', 'Geography', 'History', 'Programming'}

  
# update() - add multiple items to a set
subjects = {'Maths', 'Physics', 'Biology', 'Geography', 'History'}
subjects.update(['Programming', 'Sports', 'Communication'])
print(subjects) 
# {'Maths', 'Physics', 'Biology', 'Geography', 'History', 'Programming', 'Sports', 'Communication'}


# copy() - replicate a set
subjects = {'Maths', 'Physics', 'Biology', 'Geography', 'History'}
subjects_copy = subjects.copy('Programming')
print(subjects_copy) # {'Maths', 'Physics', 'Biology', 'Geography', 'History'}



