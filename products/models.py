from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', blank=True)
