from sys import modules

from django.db import models

# Create your models here.

class EMPLOYEES(models.Model):
    id=models.IntegerField(primary_key=True )
    name=models.CharField(max_length=100,null=False,default="employee")
    phone=models.CharField(max_length=10 )

# class STUDENTS(models.Model):
#     id=models.IntegerField(null=False, primary_key=True),
#     name=models.CharField(null=False),