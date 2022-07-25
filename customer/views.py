from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.


def register(request):
    if request.method == "POST":
        print(request.POST)
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/customer/login/')
    else:
        form = RegisterForm()
    return render(request, 'customer/register.html',{"form":form})
    

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('home')
    else:
        # Return an 'invalid login' error message.
        ...
    
    return render(request, 'customer/login.html')

def logout(request):
    logout(request)
    # return redirect('home')