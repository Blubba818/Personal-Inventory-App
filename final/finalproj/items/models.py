from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator

# Create your models here.


class Room(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='user_images/', default='rooms.jpg')
    description = models.CharField(max_length=1000, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Location(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='user_images/', default='closet.jpg')
    description = models.CharField(max_length=1000, blank=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Item(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='user_images/', default='inventory.jpg')
    description = models.CharField(max_length=1000, blank=True)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("items:item-detail", kwargs={"pk": self.pk})
