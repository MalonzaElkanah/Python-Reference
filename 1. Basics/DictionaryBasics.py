# 4. Dictionary
'''
Like a list, a dictionary is a collection of many values, but unlike indexes for lists, indexes 
for dictionaries can use many different data types, not just integers. 
Indexes for dictionaries are called keys, and a key with its associated value is called a key-value pair.
In code, a dictionary is typed with braces, {}. Example:
'''

person = {
    "name": "Elkanah",
    "gender": "Male",
    "height": "5.9 Foot",
    "weight": "67 kg",
}


# You can access these values through their keys:
print(person["name"]) # Elkanah
print(person["height"]) # 5.9 Foot


# Unlike lists, items in dictionaries are unordered. 
# It does not matter in what order the key-value pairs are typed in a dictionary:
person = {"name": "Elkanah", "gender": "Male", "Height": "5.9 Foot","Weight": "67 kg",}
person2 = {"Height": "5.9 Foot", "name": "Elkanah", "Weight": "67 kg", "gender": "Male",}
print(person==person1) # True

    
# Changing the value of a key in dictionary
person = {"name": "Elkanah", "gender": "Male", "Height": "5.9 Foot","Weight": "67 kg",}
person["name"] = "Malonza"
print(person) # {"name": "Malonza", "gender": "Male", "Height": "5.9 Foot","Weight": "67 kg",}



# Dictionary Methods
dict_methods = """
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
"""
    

# The keys(), values(), and items() Methods - will return list-like values of the 
#                                               dictionary’s keys, values, or both keys and values.
spam = {'color': 'red', 'age': 42}
v = spam.values()
print(v) # dict_values(['red', 42])

k = spam.keys()
print(k) # dict_keys(['color', 'age'])

kv = spam.items()
print(kv) # dict_items([('color', 'red'), ('age', 42)])


# The get() Method - takes two arguments: the key of the value to retrieve and 
#                       a fallback value to return if that key does not exist.
picnicItems = {'apples': 5, 'cups': 2}
print(picnicItems.get('cups', 0)) # 2
print(get('cups', 0)) # 2


# The setdefault() Method - set a value in a dictionary for a certain key only 
#                           if that key does not already have a value.
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(spam) # {'color': 'black', 'age': 5, name: 'Pooka'}

spam.setdefault('color', 'white')
print(spam) # {'color': 'black', 'age': 5, name: 'Pooka'}


# update() method - to add a new item to a dictionary, or to change the value of a current key.
spam = {'name': 'Pooka', 'age': 5}
spam.update({'color': 'black'})
print(spam) # {'color': 'black', 'age': 5, name: 'Pooka'}
spam.update({'color': 'white'})
print(spam) # {'color': 'white', 'age': 5, name: 'Pooka'}


# copy() method -  make a copy of a data dictionary to work with
spam = {'name': 'Pooka', 'age': 5}
spam_copy = spam.copy()
print(spam_copy) # {name: 'Pooka', 'age': 5}


# clear() method - remove all key-value pairs from a dictionary without deleting the entire dictionary
spam = {'name': 'Pooka', 'age': 5}
spam.clear()
print(spam) # {}


# pop() method - Removes the item specified by the key from the dictionary, and stores it in a variable.
spam = {'color': 'Black', 'name': 'Pooka', 'age': 5}
color = spam.pop("color")
print(spam) # {name: 'Pooka', 'age': 5}
print(color) # Black

    
# popitem() method -Remove the last key-value pair from a dictionary
spam = {'color': 'Black', 'name': 'Pooka', 'age': 5}
color = spam.popitem()
print(spam) # {name: 'Pooka', 'age': 5}
print(color) # ('age', 5)


# fromkeys() method - Returns a new copy of the dictionary but with only specified keys and values
spam = {'color': 'Black', 'name': 'Pooka', 'age': 5}
spam1 = dict.fromkeys(spam.keys())
results = dict.fromkeys(['Maths', 'Physics', 'Biology', 'Geography', 'History'])
print(spam1) # {'color': None, 'name': None, 'age': None}
print(results) # {'Maths': None, 'Physics': None, 'Biology': None, 'Geography': None, 'History': None}

