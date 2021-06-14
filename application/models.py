from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import Permission, User
import django
import datetime


class Course(models.Model):
	DEPARTMENT_CHOICE=(
		('Computer','Computer'),
		('IT','IT'),
		('Civil', 'Civil'),
		('Mechanical', 'Mechanical'),
		('Electrical', 'Electrical'),
	)
	name=models.CharField(choices=DEPARTMENT_CHOICE, max_length=100, default="")
	def __str__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	DEPARTMENT_CHOICE=(
		('Computer', 'Computer'),
		('IT', 'IT'),
		('Civil', 'Civil'),
		('Mechanical', 'Mechanical'),
		('Electrical', 'Electrical'),
	)

	SEMESTER_IN_COLLEGE_CHOICES = (
		(1, '1'), (2, '2'), (3, '3'), (4, '4'),
		(5, '5'), (6, '6'), (7, '7'), (8, '8'),
	)

	IDENTITY_CHOICE=(
		('faculty','Faculty'),
		('student', 'Student'),
	)
	identity=models.CharField(choices=IDENTITY_CHOICE,max_length=100,default="")
	department=models.CharField(choices=DEPARTMENT_CHOICE, max_length=100, default="")
	full_name = models.CharField(max_length = 100)
	semester = models.IntegerField(choices=SEMESTER_IN_COLLEGE_CHOICES, default="")
	enrollment = models.CharField(max_length = 200, unique=True)
	created = models.DateField(editable=False, null=True)

	def __str__(self):
		return self.enrollment

	def save(self):
		if not self.id:
			self.enrollment = self.user.username
			self.created = datetime.date.today()
		super(UserProfile, self).save()

class Assignment(models.Model):
	SEMESTER_IN_COLLEGE_CHOICES = (
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
		(6, '6'),
		(7, '7'),
		(8, '8'),
	)

	department = models.ForeignKey(Course,on_delete=models.CASCADE,default="")
	faculty = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default="")
	semester = models.IntegerField(choices=SEMESTER_IN_COLLEGE_CHOICES, default="")
	name = models.CharField(max_length = 200)
	questions = models.TextField(max_length = 1000)
	num = models.IntegerField(default=1)
	created = models.DateField(editable=False, null=True)
	updated = models.DateTimeField(editable=False, null=True)
	deadline = models.DateField(null=True)
	qsfile = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])], default=None, null=True)

	def __str__(self):
		return self.name

	def save(self):
		if not self.id:
			self.created = datetime.date.today()
		self.updated = datetime.datetime.today()
		super(Assignment, self).save()

class Solution(models.Model):
	assignment = models.ForeignKey(Assignment, models.CASCADE)

	student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
	submission_date = models.DateField()
	title=models.CharField(max_length=200,default="")
	body=models.TextField(max_length=10000,default="")
	points=models.FloatField(default=0.)
	comments=models.CharField(max_length=1000,default="")
	uploadfile = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'])])
	worked=models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def save(self):
		self.submission_date = datetime.date.today()
		super(Solution, self).save()
