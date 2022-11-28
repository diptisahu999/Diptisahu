from django.db import models

# Create your models here.

class Hospital(models.Model):
    f_name=models.CharField(max_length=30)
    l_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=15)
    password=models.CharField(max_length=32)

    def __str__(self):
        return self.l_name

class Docter(models.Model):
    f_name=models.CharField(max_length=30)
    l_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=15)
    password=models.CharField(max_length=32)
    specilist=models.CharField(max_length=32)
    pic=models.FileField(upload_to='user profile',default='avatar.png')

    def __str_(self):
        return self.f_name



