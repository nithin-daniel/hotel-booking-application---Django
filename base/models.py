from django.db import models

# Create your models here.


class HotelManager(models.Model):
    hotel_name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=500)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.hotel_name


class Rooms(models.Model):
    ROOM_CATEGORIES = (
        ('AC', 'AC'),
        ('NAC', 'Non-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )

    BED_CATEGORIES = (
        ('SI', 'Single Bed'),
        ('DB', 'Double Bed'),
        ('KS', 'King Size'),
        ('QN', 'Queen Size'),
        ('FM', 'Family Room'),
    )

    room_name = models.CharField(max_length=100)
    room_category = models.CharField(
        max_length=3, choices=ROOM_CATEGORIES, default='AC')
    bed_category = models.CharField(
        max_length=2, choices=BED_CATEGORIES, default='DB')
    capacity = models.IntegerField()
    wifi = models.BooleanField(default=True)
    tv = models.BooleanField(default=True)
    food = models.BooleanField(default=True)
    image = models.ImageField(upload_to='room_photos/', null=True)

    class Meta:
        verbose_name = "Rooms"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.room_name


class Banner(models.Model):
    image = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.image
