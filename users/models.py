from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #SI QUIERO CREAR UN SUPERUSER TENGO Q COMENTAR ESTAS LINEAS
    email = models.EmailField(unique=True)
    rut = models.IntegerField(unique=True)
    first_name = models.TextField()
    last_name = models.TextField()
    cellphone = models.TextField(default='1')
    payment_method = models.TextField()
    check_in = models.DateField()
    check_out = models.DateField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    