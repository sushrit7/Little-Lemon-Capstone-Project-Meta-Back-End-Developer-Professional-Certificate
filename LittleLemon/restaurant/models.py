from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length = 255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length = 255)
    price = models.IntegerField()
    inventory = models.IntegerField()
