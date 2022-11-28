from django.db import models

# Create your models here.
class User(models.Model):
    f_name=models.CharField(max_length=30)
    l_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=15)
    password=models.CharField(max_length=32)
    description=models.CharField(max_length=15)
    gender=models.CharField(max_length=30)

    def __str__(self):
        return self.l_name
    
class Appo(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
    time=models.CharField(max_length=30)

    def __str__(self):
        return self.name



