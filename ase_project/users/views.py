from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
# 		print(form)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! You are now able to log in')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/login_register.html', {'form': form})


def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'Your account has been created! You are now able to log in')
			return redirect('landing')
	else:
		form=UserRegisterForm()
	return render(request,'users/login_register.html')

# View for login functionality
def Login(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			form = login(request,user)
			user=request.user
			messages.success(request,f'You are successfully logged in!!')
			user.save()
			return redirect('landing')
		else:
			messages.info(request,f'Account done, please login')
	form=AuthenticationForm()
	return render(request,'users/login_register.html',{'form':form})



@login_required
def profile(request):
	return render(request, 'users/profile.html')

def volunteer(request):
	return render(request,'users/volunteer.html')