from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from profiles.forms import  UserUpdateForm, ProfileUpdateForm
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout

# View for signup/register functionality
def register(request):
	# Checking for a POST request
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		# Checking if details in the form are valid
		if form.is_valid():
			# We save the object temporarily and not commit
			user = form.save(commit=False)
			# We activate a user account after email confirmation
			user.is_active=False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your HomeChef account.'
			message = render_to_string('users/acc_active_email.html',{
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
				})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
				mail_subject,message, to=[to_email]
			)
			# Email for account verification sent
			email.send()
			return render(request,'users/email_confirm_request.html')
	else:
		form = UserRegisterForm()
	form2 = AuthenticationForm()
	return render(request,'users/login_register.html',{'form':form,'form2':form2})

# View for login functionality
def login_view(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		# User authenticated
		user = authenticate(request, username=username, password=password)
		if user is not None:
			# User logged in
			login(request,user)
			messages.success(request,f'You are successfully logged in!!')
			return redirect('Buy')
		else:
			messages.info(request,f'Please verify the details and login again')
			form = UserRegisterForm()
			form2 = AuthenticationForm()
			return render(request,'users/login_register.html',{'form':form,'form2':form2})
	else:
		form = UserRegisterForm()
		form2 = AuthenticationForm()
		return render(request,'users/login_register.html',{'form':form,'form2':form2})

# View for activation link
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # Verified the user, thus made active
        user.is_active = True
        user.save()
		# Logged in
        login(request, user)
        return render(request,'users/email_confirm.html')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
def profile(request):
	if request.method == 'POST':
	   u_form = UserUpdateForm(request.POST, instance=request.user)
	   p_form = ProfileUpdateForm(request.POST,
								  request.FILES,
								  instance=request.user.profile)
	   if u_form.is_valid() and p_form.is_valid():
		   u_form.save()
		   p_form.save()
		   messages.success(request, f'Your account has been updated!')
		   return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form':u_form,
		'p_form':p_form,
	}
	return render(request, 'users/profile.html', context)