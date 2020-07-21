from django import forms
from .models import Profile, VolunteerModel
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField
	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['phone_number', 'image']


class VolunteerForm(forms.Form):
	address = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class': 'input1', 'type': 'text', 'name': 'address', 'placeholder': 'Address'
	}))
	city = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class': 'input1', 'type': 'text', 'name': 'city', 'placeholder': 'City'
	}))
	state = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class': 'input1', 'type': 'text', 'name': 'state', 'placeholder': 'State'
	}))
	pincode = forms.CharField(required=True, widget=forms.TextInput(attrs={
		'class': 'input1', 'type': 'text', 'name': 'pincode', 'placeholder': 'Pincode'
	}))
	
class VolunteerUpdateForm(forms.ModelForm):
	class Meta:
		model = VolunteerModel
		fields = ['address','city','state','pincode']