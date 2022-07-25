from django.shortcuts import render
from owner.models import Banner

def index(request):
    banner = Banner.objects.all()
    current_user = request.user
    context = {
        'banner' : banner,
        'current_user':current_user,
    }
    return render(request, 'index.html',context)