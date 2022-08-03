from django.shortcuts import render
from .models import Banner

# Create your views


def index(request):
    banner = Banner.objects.all()
    current_user = request.user
    context = {
        'banner': banner,
        'current_user': current_user,
    }
    return render(request, 'index.html', context)

def account_profile(request):
    return render(request, 'owner/profile.html')

def my_rooms(request):
    return render(request, 'owner/my_rooms.html')