from django.shortcuts import render, redirect
from django.contrib import messages
from profiles.forms import  UserUpdateForm, ProfileUpdateForm
from .forms import UserRegisterForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def register(request):
	if request.method=='POST':
		form = UserRegisterForm(request.POST)
		print(request.POST.get('username'))
		print(request.POST.get('first_name'))
		print(request.POST.get('last_name'))
		print(request.POST.get('email'))
		print(request.POST.get('password1'))
		print(request.POST.get('password2'))
		print(form.is_valid())
		print(form.errors)
		if form.is_valid():
			form.save()
			user = form.save(commit=False)
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
			email.send()
			return render(request,'users/email_confirm_request.html')
	else:
		form=UserRegisterForm()
	return render(request,'users/login_register.html',{'form':form})
		



# View for login functionality
def Login(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			form = login(request,user)
			user=request.user
			messages.success(request,f'You are successfully logged in!!')
			user.save()
			print("landing")
			return redirect('landing')
		else:
			messages.info(request,f'Please verify the details and login again')
	form=AuthenticationForm()
	return render(request,'users/login_register.html',{'form':form})
  	
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
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