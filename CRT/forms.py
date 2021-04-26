from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from django.contrib.auth import models
from CRT.models import Complaintbox,ImProfile
class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=['username']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"username" }),
		"password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"password" }),
		}

class ComplaintForm(forms.ModelForm):
	class Meta:
		model=Complaintbox
		fields="__all__"


class UtupForm(forms.ModelForm):
	class Meta:
		model=User
		fields=["username","email"]
		widgets= {
		"username":forms.TextInput(attrs = {"class": "form-control","placeholder":"Enter your name","required":True}),
		"email":forms.EmailInput(attrs = {"class": "form-control","placeholder":"Enter your Email","required":True}),
		}

class ImForm(forms.ModelForm):
	class Meta:
		model=ImProfile
		fields=["age","gender","impf"]
		widgets= {
		"age":forms.NumberInput(attrs = {"class": "form-control","placeholder":"Update your age","required":True}),
		"gender":forms.Select(attrs = {"class": "form-control",}),
		 
		}

class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter your old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter your new password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter your new confirmation password"}))
	class Meta:
		model=User
		fields=["password"]


