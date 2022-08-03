from django.urls import path
from .  import views
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/',views.account_profile,name="profile"),
    path('myrooms/',views.my_rooms,name="my_rooms"),
]

