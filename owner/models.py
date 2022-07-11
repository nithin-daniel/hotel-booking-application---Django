from django.db import models

# Create your models here.

class HotelManager(models.Model):
    hotel_name = models.CharField(max_length=100,blank=False)
    location = models.CharField(max_length=500)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.hotel_name
