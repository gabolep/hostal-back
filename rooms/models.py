from django.db import models
from users.models import User
from django.db.models import SET_NULL

class Room(models.Model):
    number = models.IntegerField(unique=True, primary_key=True)
    type = models.CharField(max_length=255)
    bed = models.CharField(max_length=255)
    floor = models.IntegerField()
    price = models.IntegerField()
    deluxe = models.BooleanField(default=False)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return self.number