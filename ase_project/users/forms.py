from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	# name = forms.CharField()
	email = forms.EmailField(label='Email Address')
	class Meta:
		model = User
		fields = ['username','email','password1','password2']