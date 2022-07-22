from django.shortcuts import render,redirect
from .forms import RegisterForm

# Create your views here.
def login(request):
    return render(request, 'customer/login.html')

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
    
 