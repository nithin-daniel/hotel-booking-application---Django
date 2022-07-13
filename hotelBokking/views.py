from django.shortcuts import render
from owner.models import Banner

def index(request):
    banner = Banner.objects.all()
    context = {
        'banner' : banner,
    }
    return render(request, 'index.html',context)