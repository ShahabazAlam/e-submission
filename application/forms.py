from django import forms
from django.contrib.auth.models import User
from .models import Assignment, Solution, UserProfile
import datetime

# class AlbumForm(forms.ModelForm):
#
#     class Meta:
#         model = Album
#         fields = ['artist', 'album_title', 'genre', 'album_logo']
class SolutionForm(forms.ModelForm):
	class Meta:
		model = Solution
		fields = ['title','body', 'uploadfile']

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		usr_semester = UserProfile.objects.get(user=user).semester
		course=kwargs.pop('course')
		# print("##############" + str(usr_year))
		# usr_assign = Assignment.objects.filter(year=usr_year)
		super(SolutionForm, self).__init__(*args, **kwargs)
		self.fields['uploadfile'].required = False
		#self.fields['assignment'].queryset = Assignment.objects.filter(year=usr_year,course__name=course)

class DateInput(forms.DateInput):
    input_type = 'date'

class AssignmentForm(forms.ModelForm):
	class Meta:
		model=Assignment
		fields=['num','semester','name','questions','deadline','qsfile']
		widgets = {
			'deadline': DateInput()
		}
		deadline = forms.DateField(input_formats=['%d-%m-%Y'])
	def __init__(self, *args, **kwargs):
		super(AssignmentForm, self).__init__(*args, **kwargs)
		self.fields['qsfile'].required = False

class SolCreditForm(forms.ModelForm):
	class Meta:
		model=Solution
		fields=['points','comments']


class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=50, required=True)
	email = forms.EmailField(max_length=250, required=True)
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ['username', 'email', 'password']
		help_texts = {
			'username': 'Enter Enrollment Number',
		}

	def clean(self):
		cleaned_data = super(UserForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")

		if password != confirm_password:
			raise forms.ValidationError("password does not match")

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['full_name', 'department', 'identity', 'semester',]
