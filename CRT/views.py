from django.shortcuts import render,redirect
from CRT.forms import UsForm,ComplaintForm,ImForm,UtupForm,ChpwdForm
from django.core.mail import send_mail
from Campus import settings
from django.contrib import messages
from django.contrib.auth.models import User 
from CRT.models import ImProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')
def authuser(request):
	return render(request,'html/authuser.html')

def beforereg(request):
	# if request.method == "POST":
	# 	t = UsForm(request.POST)
	# 	if t.is_valid():
	# 		t.save()
	# 		return redirect('/lg')
	# t = UsForm()
	return render(request,'html/beforeregestration.html')

def regi(request):
	if request.method == "POST":
		t = UsForm(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/lg')
	t = UsForm()
	return render(request,'html/register.html',{'u':t})
@login_required
def dashboard(req):
	return render(req,'html/dashboard.html')
@login_required
def profile(req):
	return render(req,'html/profile.html')

def complaint(req):
	if req.method== "POST":
		data=ComplaintForm(req.POST)
		if data.is_valid():
			subject='Confirmation_complaint'
			body="Thank you for complaint"+req.POST['p_name']
			receiver=req.POST['p_email']
			sender= settings.EMAIL_HOST_USER
			send_mail(subject,body,sender,[receiver])
			data.save()
			messages.success(req,"Successfully sent to your mail"+receiver)
			return redirect('/')
	form=ComplaintForm()
	return render(req,'html/complaint.html',{'c':form})
@login_required
def updf(request):
	if request.method == "POST":
		u=UtupForm(request.POST,instance=request.user)
		i=ImForm(request.POST,instance=request.user.improfile)
		if u.is_valid() and i.is_valid():
			u.save()
			i.save()
			return redirect('/pro')
	u=UtupForm(instance=request.user)
	i=ImForm(instance=request.user.improfile)
	return render(request,'html/updateprofile.html',{'us':u,'imp':i})
@login_required
def cgf(request):
	if request.method == "POST":
		c=ChpwdForm(request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/lg')
	c=ChpwdForm(user=request)
	return render(request,'html/changepassword.html',{'p':c})

def acheivements(request):
	return render(request,'html/acheivements.html')

# def sign(request):
# 	if request.method == "POST":
# 		t = UsForm(request.POST)
# 		if t.is_valid():
# 			t.save()
# 			return redirect('/lg')
# 	t = UsForm()
# 	return render(request,'html/signin.html',{'u':t})

# @login_required
# def signout(request):
# 	return render(request,'html/singout.html')