# Files and File Paths


This section involves how to use Python to create, read, and save files on the hard drive. 
The files can be both text or binary files. It also involves organize preexisting files on the hard drive 
For Instance: copying, renaming, moving, or compressing them.



#'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 
['dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 
'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 
'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 
'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']
#
# os.path.join(<folder>, <folder>, ...)    -   return os specific file path

# os.getcwd()       -   get current working directory
# os.chdir(<path>)  -   change directory
# os.makedirs(<path>)   -   create new folder/directory

# os.path.abspath(<path>)   -   will return a string of the absolute path of the argument.
# os.path.isabs(path)   -   return True if the argument is an absolute path and False if it is a relative path.
# os.path.relpath(path, start)  -   return a string of a relative path from the start path to path .
# If start is not provided, the current working directory is used as the start path.
# os.path.dirname(path)    -    return a string of everything that comes before the last slash in the path argument.
# os.path.basename(path)    -   return a string of everything that comes after the last slash in the path argument.
# os.path.split()   -   to get a tuple value with these two strings dirname and basename
# os.path.getsize(path)    -    return the size in bytes of the file in the path argument.
# os.path.exists(path)  -   return True if the file or folder referred to in the argument exists otherwise False
# os.path.isfile(path)     -    return True if the path argument exists and is a file and will return False otherwise.
# os.path.isdir(path)   -   return True if the path argument exists and is a folder and will return False otherwise.

# os.listdir(path)  -   return a list of filename strings for each file in the path argument.


# The File Reading/Writing Process
#
# open()    -   function to return a File object. default read mode
# open('<file 2 open>', 'w')    -   open file for writing   'a' - append file
# read() or write(<text to write/append>)    -    method on the File object.
# readlines() method to get a list of string values from the file, one string for each line of text.
# close()   -   Close the file by calling the method on the File object.
# n


# Saving Variables with the shelve Module -
#
# You can save variables in your Python programs to binary shelf files using the shelve module.
#
# shelfFile = shelve.open(<filename>)
#
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()
# 

shelfFile = shelve.open('mydata')
shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
shelfFile.close()

import os

os.path.join('usr', 'bin', 'spam')
print(os.path.join('usr', 'bin', 'spam'))
