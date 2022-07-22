from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	# def _init_(self, *args, **kwargs):
	# 	super(UserCreateForm, self)._init_(*args, **kwargs)

	# 	for fieldname in ['username', 'password1', 'password2']:
    #     	self.fields[fieldname].help_text = None