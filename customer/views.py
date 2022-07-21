from django.shortcuts import render,redirect
from .forms import RegisterForm
# Create your views here.
def login(request):
    return render(request, 'customer/login.html')

def register(request):

    return render(request, 'customer/register.html')
    