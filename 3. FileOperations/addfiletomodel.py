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




# SECOND USE CASE OF ADD TO MODEL 09/11/2021
from cvletters.models import CV, CoverLetter
from cvletters.forms import CVForm, CoverLetterForm
#from settings.models import UserProfile, AppSettings
from jobprofiles.models import JobProfile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
import os
path = '/home/malone/Django Projects/Job-Application-Bot/authentication/Uploads/letter-templates/'
for folderName, subfolders, filenames in os.walk(path):
	for filename in filenames:
		# job_profile
		profiles = JobProfile.objects.all()
		job_profile = profiles[0] 
		# name
		q = filename.split('-')
		name = q[-1]
		# binary_data
		binary_data = "b''"
		# description 
		description = "Resume Marker Templates - " + str(q[0])
		# status,
		status = "template"
		# file
		category = q[0]
		f_path = path+filename
		with open(f_path) as f:
			# job_profile, name, file, binary_data, description, status
			file = File(f)
			data = CoverLetter(job_profile=job_profile, name=name, file=file, binary_data=binary_data, description=description, status=status)
			data = data.save()
			print(data)




