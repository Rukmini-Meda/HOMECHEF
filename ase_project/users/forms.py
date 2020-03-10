from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField
	types = forms.ChoiceField(choices = (('CR', 'Customer'),('VN', 'Vendor')))
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','types','password1','password2']



