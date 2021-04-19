# COPYING FILES #
# import shutil     -   shell Utility
# shutil.copy('source', 'destination')      -   will copy a single file
# shutil.copytree(source, destination)      -   will copy the folder with all of its files and subfolders


# MOVING FILES and FOLDERS
# shutil.move(source, destination)


# Permanently Deleting Files and Folders
# os.unlink(path)       -   will delete the file at path .
# os.rmdir(path)        -   will delete the folder at path . This folder must be empty of any files or folders.
# shutil.rmtree(path)   -  will remove the folder at path , and all files and folders it contains will also be deleted


# Safe Deletes with the send2trash Module
# import send2trash
# send2trash.send2trash('bacon.txt')


# Walking THROUGH a Directory Tree
# os.walk('C:\\delicious')  -   will return three values on each iteration through A for loop
# 1. A string of the current folder’s name
# 2. A list of strings of the folders in the current folder
# 3. A list of strings of the files in the current folder
#
#
#
# d


import os

for folderName, subfolders, filenames in os.walk('/home/malone/PycharmProjects'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)
            print('')
