from django.shortcuts import render

# Create your views
def account_profile(request):
    return render(request, 'owner/profile.html')

def my_rooms(request):
    return render(request, 'owner/my_rooms.html')