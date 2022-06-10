from django.db import models
from users.models import User
from rooms.models import Room
from django.db.models import CASCADE

class Reservation(models.Model):
    reservation_number = models.IntegerField(unique=True, primary_key=True)
    user = models.ForeignKey(User,on_delete=CASCADE)
    room = models.ForeignKey(Room, on_delete=CASCADE)
    payment_method = models.TextField()
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return self.number