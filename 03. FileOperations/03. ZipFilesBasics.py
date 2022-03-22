# Reading ZIP Files
# import zipfile
# exampleZip = zipfile.ZipFile('example.zip')
# exampleZip.namelist()    -   method returns a list of strings for all the files and folders contained in the ZIP file
# spamInfo = exampleZip.getinfo('spam.txt')
# >>> spamInfo.file_size
# 13908
# >>> spamInfo.compress_size
# 3828
# u >>> 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
# .compress_size, 2))
# 'Compressed file is 3.63x smaller!'
# >>> exampleZip.close()


# Extracting from ZIP Files
# exampleZip = zipfile.ZipFile('example.zip')
# exampleZip.extractall()
# exampleZip.close()

# Creating and Adding to ZIP Files
# newZip = zipfile.ZipFile('new.zip', 'w')  -   pass 'a' as the second argument to open the ZIP file in append mode.
# newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()
