from django.db import models
from datetime import datetime
# Create your models here.

class EMPLOY(models.Model):
    id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    emp_mob=models.CharField(max_length=100)
    emp_doj=models.DateTimeField(default=datetime.now)
