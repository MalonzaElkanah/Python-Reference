import sys
import os
import shutil
import datetime
import re


def set_file_type():
    audios = ['mp3', 'aac']
    videos = ['mp4', 'mpeg', 'vddl', 'opus', 'vob', 'mkv']
    documents = ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'epub', 'txt', 'xls']
    apps = ['apk', 'exe', 'taz']
    compressed = ['zip', 'rar']
    pictures = ['jpg', 'png', 'jpeg', 'webp', 'gif', 'icon']
    all_above = {"AUDIOS": audios, "VIDEOS": videos, "DOCUMENTS": documents, "APPS": apps,
                 "COMPRESSED": compressed, "PICTURES": pictures}
    print("########## select file type for extraction #########")
    print("ENTER:")
    i = 1
    for a in all_above.items():
        print(i, "for", a[0], ": ", a[1])
        i += 1
    print(i, "All of Above ")
    print(i+1, "None of Above: Specify File extension")
    print('0 to EXIT', "\n")
    try:
        choice = int(input("CHOICE: "))
        while not ((i + 1) >= choice >= 0):
            print("ERROR: INVALID Choice, Try Again!!!")
            choice = int(input("CHOICE: "))
        if choice == i:
            print("CHOICE: ALL OF ABOVE!!!")
            return audios + videos + documents + apps + compressed + pictures
        elif choice == (i + 1):
            file_type = [input("Specify FILE EXTENSION: ")]

            return file_type
        elif choice == 0:
            print("Exit...")
            sys.exit()
        else:
            j = 1
            for a in all_above.keys():
                if j == choice:
                    print("CHOICE: ", a)
                    return all_above.__getitem__(a)
                j += 1
    except ValueError:
        print("Invalid Input: Number Input Only")
        sys.exit()


def set_extraction_location():
    print("\nSearch and Extraction Location.\nDefault:", os.getcwd(), "(the current working directory) ")
    bol = input("DO YOU WANT TO CHANGE [Y/n]: ")
    while bol.upper() not in ['Y', 'N']:
        print("ERROR: INVALID INPUT - Choose Y or N")
        bol = input("DO YOU WANT TO CHANGE [Y/n]: ")
    if bol.upper() == 'Y':
        print("\nchanging Extraction Location...")
        new_loc = input("ENTER NEW EXTRACTION LOCATION: ")
        while not os.path.isdir(new_loc):
            print("ERROR: INVALID Directory Location, Try Again!!!")
            new_loc = input("ENTER NEW EXTRACTION LOCATION: ")
        if os.path.isdir(new_loc):
            return new_loc
    elif bol.upper() == 'N':
        return os.getcwd()


def set_destination_location():
    print("\nDestination Location.\nDefault:", os.getcwd(), "(the current working directory) ")
    bol = input("DO YOU WANT TO CHANGE [Y/n]: ")
    while bol.upper() not in ['Y', 'N']:
        print("ERROR: INVALID INPUT - Choose Y or N")
        bol = input("DO YOU WANT TO CHANGE [Y/n]: ")
    if bol.upper() == 'Y':
        print("\nchanging Destination Location...")
        new_loc = input("ENTER NEW DESTINATION LOCATION: ")
        while not os.path.isdir(new_loc):
            print("ERROR: INVALID Directory Location, Try Again!!!")
            new_loc = input("ENTER NEW EXTRACTION LOCATION: ")
        if os.path.isdir(new_loc):
            return new_loc
    elif bol.upper() == 'N':
        return os.getcwd()


def extract_files(file_types, location, destination):
    folder = str(datetime.datetime.now())
    pattern = re.compile(r':+|\.+|-+|' '')
    folder = pattern.sub('', folder)

    destination = destination+'/extractedFiles'+folder+'/'
    pattern = re.compile(r'//+')
    destination = pattern.sub('/', destination)
    os.makedirs(destination)
    print(destination)
    for folderName, sub_folders, file_names in os.walk(location):
        print('\nSearching in ' + folderName)
        print('SUB-FOLDERS:')
        i = 0
        for sub_folder in sub_folders:
            i += 1
            print('\t', sub_folder)
        if i == 0:
            print("\t0 sub-folders found ")

        print('Files:')
        j = 0
        for filename in file_names:
            j += 1
            print('\t',  filename)
            file_prop = str(filename).split('.')
            if file_prop[-1].upper() in str(file_types).upper():
                if not os.path.isdir(destination+file_prop[-1]+'/'):
                    os.makedirs(destination+file_prop[-1]+'/')
                print('\t\t\t', file_prop[-1], 'match found')
                print('\t\t\t', 'COPYING TO DESTINATION...')
                if not os.path.isfile(destination+file_prop[-1]+'/'+filename):
                    shutil.copy(folderName + '/' + filename, destination+file_prop[-1]+'/')
                
        if j == 0:
            print("\t0 files found ")


k = set_file_type()
print(k)
loc = set_extraction_location()
print(loc)
d_loc = set_destination_location()
print(d_loc)
extract_files(k, loc, d_loc)
