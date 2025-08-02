from django.db import models

# Create your models here.
class USER(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100,unique=True)
    phone=models.CharField(max_length=10,unique=True)
    email=models.CharField(max_length=100,unique=True)