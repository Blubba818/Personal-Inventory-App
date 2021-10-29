from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Room(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', default='images/rooms.jpg')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Location(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', default='images/closet.jpg')
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Item(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', default='images/inventory.jpg')
    description = models.CharField(max_length=1000)
    quantity = models.IntegerField(default=1)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("items:item-detail", kwargs={"pk": self.pk})
