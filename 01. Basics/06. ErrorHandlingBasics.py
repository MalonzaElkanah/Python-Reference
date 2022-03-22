'''
            ### 1.8 Handling the error and exceptions - try..except..else..finally
'''

# Getting an error, or exception, in your Python program means the entire program will crash. 
# You don’t want this to happen in real-world programs. Example:
dummy_file = open('random_file.csv')
# FileNotFoundError: [Errno 2] No such file or directory: 'random_file.csv'

# Above program creates a FileNotFoundError and stops executing. We want the program to detect errors, 
# handle them, and then continue to run. Thats where try...except...else...finally... Statements comes in.

try:
    # Open file and shows its name.
    dummy_file = open('random_file.csv')
    print(dummy_file.name)
except Exception:
    print("Sorry, File named random_file.csv Does not Exist.")

"""
            Being Specific about Exceptions
"""
# if any exception is raised in this try block, it will execute the code in except block. 
# Sometimes we need to catch a specific error. For Instance, FileNotFoundError in above code. 
# You add the exception name after the except statement.
try:
    # Open file and shows its name.
    dummy_file = open('random_file.csv')
    print(dummy_file.name)
except FileNotFoundError:
    print("Sorry, File named random_file.csv Does not Exist.")


"""
            One Try statement can be followed by multiple except statement.
"""
try:
    ...
except FileNotFoundError:
    print("Sorry, File named random_file.csv Does not Exist.")
except Exception as e:
    print(e)


"""
            *else block*  
"""
# Code in this block will be executed if no exceptions raised 
try:
    ...
except FileNotFoundError:
    print("Sorry, File named random_file.csv Does not Exist.")
except Exception as e:
    print(e) 
else:
    # Continue on here only if no exceptions raised

    
"""
            *finally block*
"""
# if included, the code in this block will run whether an exception occurs or not.
try:
    # try to do this
except:
    # if x happens, stop here
except Exception as e:
    # if something else bad happens, stop here
else:
    # if no exceptions, continue on normally here
finally:
    # do this code no matter what happened above

