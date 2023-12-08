from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    place=models.CharField(max_length=50)
    salary=models.IntegerField()
    

# das