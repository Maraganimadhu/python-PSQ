from django.db import models

# Create your models here.
class STUDENT(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
