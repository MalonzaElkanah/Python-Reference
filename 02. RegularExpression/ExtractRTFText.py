# A program to extract text from rtf files and dump them to text file.
import os
from striprtf.striprtf import rtf_to_text


# Step One: Get the RTF files location
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


# Step Two: Extract Text from RTF file
def extarct_rtf_text(file_location):
	# Get the file name
	file_name = os.path.basename(file_location)
	# Get the file extension
	file_data = file_name.split('.')
	file_extn = file_data[-1]
	# Check if File is an RTF File
	if file_extn == 'rtf':
		print("\nExtracting Text from LOCATION://"+file_location+"...")
		file = open(file_location)
		f_content = file.read()
		text = rtf_to_text(f_content)
		return [file_data[0], text]
	else:
		return False


# Step Three: Save extracted Text to TXT file
def save_to_txt(text_data, save_location):
	# 
	location = os.path.join(save_location, 'text_data')
	url_file = open(location+'/'+text_data[0]+'.txt', 'a')
    url_file.write(save_location)


# Step Four: Bringing all Above steps Together
location = 
