from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			first_name = form.cleaned_data.get('first_name')
			messages.success(request, f'Account created for {first_name}!!! Login to proceed')
			return redirect('login')

	else:
		form = UserRegisterForm()
	return render(request, "users/register.html", {'form': form})

@login_required
def profile(request):
	return render(request, 'users/profile.html')