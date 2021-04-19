import os


def extract_files():
    location = os.getcwd()
    audios = ['mp3', 'aac']
    videos = ['mp4', 'mpeg', 'vddl', 'opus', 'vob', 'mkv']
    documents = ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'epub', 'txt', 'xls']
    apps = ['apk', 'exe', 'taz']
    compressed = ['zip', 'rar']
    pictures = ['jpg', 'png', 'jpeg', 'webp', 'gif', 'icon']
    file_types = audios + videos + documents + apps + compressed + pictures
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
                print('\t\t\t', file_prop[-1], 'match found')
                print('\t\t\t', 'COPYING TO DESTINATION...')
        if j == 0:
            print("\t0 files found ")


extract_files()