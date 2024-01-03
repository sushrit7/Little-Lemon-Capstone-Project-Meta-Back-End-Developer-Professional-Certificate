from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length = 255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField()

class MenuItem(models.Model):
    title = models.CharField(max_length = 255)
    price = models.IntegerField()
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
