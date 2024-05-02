from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDER_CHOICES = (
        ("M", "Man"),
        ("W", "Woman"),
    )
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=50)
    birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    intro = models.TextField(blank=True)
    REQUIRED_FIELDS = ['name', 'nickname', 'birth']
