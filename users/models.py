from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #SI QUIERO CREAR UN SUPERUSER TENGO Q COMENTAR ESTAS LINEAS
    email = models.EmailField(unique=True)
    rut = models.IntegerField(unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    cellphone = models.TextField(default='1')
    is_admin = models.BooleanField(default=False)
    has_booking = models.BooleanField(default=False)
    date_of_birth = models.DateField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    