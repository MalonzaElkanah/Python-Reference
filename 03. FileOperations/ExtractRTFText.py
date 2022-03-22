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
	# Get saving location
	location = os.path.join(save_location, 'text_data')
	if not os.path.exists(location):
		os.makedirs(location)
	# Open file for saving
	url_file = open(location+'/'+text_data[0]+'.txt', 'a')
	# Save the extracted text
	url_file.write(text_data[1])
	print("\nSaved Extracted Text to LOCATION://"+location+"/"+text_data[0]+".txt")



# Step Four: Bringing all Above steps Together
location = set_files_location()
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
		rtf_data = extarct_rtf_text(folderName + '/' + filename)
		if rtf_data != False:
			save_to_txt(rtf_data, location)
	if j == 0:
		print("\t0 files found ")

