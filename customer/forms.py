from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(help_text=None,widget=forms.PasswordInput())
	# def _init_(self, *args, **kwargs):
	# 	super(UserCreateForm, self)._init_(*args, **kwargs)
	# 	for fieldname in ['username', 'password1', 'password2']:
	# 		self.fields[fieldname].help_text = None 
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		labels = {
            'password1': 'Password',
        }
		help_texts = {
            'username': None,
            'email': None,
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)