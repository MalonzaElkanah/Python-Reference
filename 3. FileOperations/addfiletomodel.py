from jobs.models import SavedJobs, MyCv, MyLetter
from jobs.forms import SavedJobsForm, CVForm, LetterForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
import os
path = '/home/malone/PycharmProjects/DjangoProjects/Elkanah/malone/Uploads/File/Jobs/MyLetters/Sample Letters/'
for folderName, subfolders, filenames in os.walk(path):
	for filename in filenames:
		q = filename.split('-')
		name = q[-1]
		category = q[0]
		f_path = path+filename
		with open(f_path) as f:
			# name, file, category, description, date_created, status
			d = {'name': name, 'category': category, 'description': 'Resume Marker Templates', 'status': 'Template'}
			file = File(f)
			# file_data = {'file': SimpleUploadedFile(filename, file)}
			data = MyLetter(name=name, file=file, category=category, description='Resume Marker Templates', status='Template')
			data = data.save()
			print(data)

