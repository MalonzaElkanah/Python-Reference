# A program to change normal url (href="index.html") to django specific url (href="{% url 'index'%}")
import os
import re


app_name = ''

# Step ONE - Read an HTML File
def get_html_file(path):
    if os.path.isfile(path):
        data = path.split('.')
        if data[-1].lower() in ['html', 'htm']:
            d_file = open(path)
            return d_file.read()
        else:
            print(False, "File is not an HTML File")
            return False
    else:
        os.getcwd()
        print(False, os.getcwd())
        return False


# Step Two - write a pattern to find href="index.html"
def set_pattern():
    pattern0 = re.compile(r'href="\w+-*\w+-*\w+-*\w+-*\w+\.html"')
    pattern1 = re.compile(r'href="')
    pattern2 = re.compile(r'\.html"')
    pattern = [pattern0, pattern1, pattern2]
    return pattern


def set_static_pattern(var):
    # href: png, css, js, jpg, jpeg, gif, svg, ico, eot ttf, woff, woff2
    exts = ['png', 'css', 'js', 'jpg', 'jpeg', 'gif', 'svg', 'ico', 'eot', 'ttf', 'woff', 'woff2', 'min.css', 'min.js']
    patterns = {}
    for ext in exts:
        pattern0 = re.compile(r''+var+r'="assets/\w+/*\w*/*\w*/*\w*/*\w*/*\w*/*\w*/*\w*/*\w*-*\w*-*\w*\.'+ext+r'"')
        pattern1 = re.compile(r''+var+r'="assets/')
        pattern2 = re.compile(r'\.'+ext+'"')
        pattern = [pattern0, pattern1, pattern2]
        patterns.setdefault(ext, pattern)
    return patterns


# Step THREE - match the pattern to HTML file
def match(pattern, text):
    init_txt = re.findall(pattern[0], text)
    for ptn_txt in init_txt:
        if not ptn_txt == '':
            new_ptn = re.compile(r''+ptn_txt+r'')
            txt = pattern[1].sub('', ptn_txt)
            txt = pattern[2].sub('', txt)
            django_url = 'href="{% url \''+txt+'\' %}"'
            text = new_ptn.sub(django_url, text)
            record_changes(txt)
            
    return text


def match_static(patterns, text, var):
    # href="{% static 'administrator/img/favicon.png' %}"
    for ext, pattern in patterns.items():

        init_txt = re.findall(pattern[0], text)
        for ptn_txt in init_txt:
            if not ptn_txt == '':
                new_ptn = re.compile(r''+ptn_txt+r'')
                txt = pattern[1].sub(var+'="{% static \''+app_name+'/', ptn_txt)
                txt = pattern[2].sub('.'+ext+'\' %}"', txt)
                static_url = txt
                text = new_ptn.sub(static_url, text)
                record_static(static_url)
            
    return text


def update_url(new_text, html_file):
    new_file = open(html_file, 'w')
    new_file.write('{% load static %}\n')
    new_file.close()
    new_file = open(html_file, 'a')
    new_file.write(new_text)
    print("URLS updated...")


def record_changes(txt):
    url_txts = txt.split('-')
    name = ''
    view = ''
    for y in url_txts:
        if url_txts[-1] == y:
            name = name + y
            view = view + y
        else:
            name = name + y + '-'
            view = view + y + '_'
    url_file = open('urls_changed.txt', 'a')
    url_file.write('url(r\'^'+name+'/\', views.'+view+', name = \''+name+'\'),\n')
    view_file = open('view_created.txt', 'a')
    view_file.write('def '+view+'(request):\n')
    view_file.write('   return render(request, \''+app_name+'/'+name+'.html\')\n')
    view_file.write('\n')
    view_file.write('\n')
    print("URLS updated...")


def record_static(static_url):
    url_file = open('static_urls.txt', 'a')
    url_file.write(static_url+'\n')
    print("STATIC URLS updated...")


def set_files_location():
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


def set_app_name():
    return str(input("App Name: "))


def remove_repeated_lines(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    k = 1
    num = len(lines)
    for line in lines:
        i = k
        while i < num:
            if line == lines[i]:
                del lines[i]
                num -= 1
            else:
                i += 1
        k += 1
    file = open(file_name, 'w')
    file.flush()
    file.close()
    for line in lines:
        file = open(file_name, 'a')
        file.write(line)
        file.close()



def replace_urls(location):

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
            print('\t', filename)
            html_text = get_html_file(folderName + '/' + filename)
            if html_text:
                print('\t\t\t',  'HTML file', 'match found')
                try:
                    ptn = set_pattern()
                    match_data = match(ptn, html_text)
                    ptn2 = set_static_pattern('href')
                    match_data2 = match_static(ptn2, match_data, 'href')
                    ptn2 = set_static_pattern('src')
                    match_data3 = match_static(ptn2, match_data2, 'src')
                    update_url(match_data3, folderName + '/' + filename)
                except Exception:
                    print("UnicodeDecodeError Detected")

        if j == 0:
            print("\t0 files found ")


loc = set_files_location()
app_name = set_app_name()
replace_urls(loc)
remove_repeated_lines('urls_changed.txt')
remove_repeated_lines('view_created.txt')
