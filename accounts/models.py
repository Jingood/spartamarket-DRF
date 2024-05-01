from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=50)
    birth = models.DateField()
    REQUIRED_FIELDS = ['name', 'nickname', 'birth']
