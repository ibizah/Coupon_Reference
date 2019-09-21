from django.db import models
from django.forms import ModelForm


# Create your models here.

class User(models.Model):
    
    name= models.CharField(max_length=200)
    email= models.EmailField(max_length=100)
    age= models.IntegerField()
    city= models.CharField(max_length=100)
    referal_code= models.CharField(max_length=7,unique=True)

    def __str__(self):
        return self.name
