from django.db import models

# Create your models here.
class EMPLOYEE(models.Model):
    id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=20)
    emp_age=models.IntegerField(null=False)
    