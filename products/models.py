from django.db import models

# Create your models here.
class Product(models.Model):
    type=models.CharField(max_length=100)
    image=models.CharField(max_length=600)
    size=models.CharField(max_length=100)
    price=models.IntegerField()
