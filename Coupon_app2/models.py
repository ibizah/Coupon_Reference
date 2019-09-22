from django.db import models
from django.forms import ModelForm
import string, random


# Create your models here.

class User(models.Model):

    name= models.CharField(max_length=200)
    email= models.EmailField(max_length=100)
    age= models.IntegerField()
    city= models.CharField(max_length=100)
    referal_code = models.CharField(max_length=300, blank=True, null=True)


    def generate_verification_code(self):
        newreferal_code = ''.join([''.join(random.sample(string.ascii_letters, 2)),''.join(random.sample(string.digits, 2)),''.join(random.sample(string.ascii_letters, 3))])
        return newreferal_code

    def save(self, *args, **kwargs):
        if not self.pk:
            self.referal_code = self.generate_verification_code()
        elif not self.referal_code:
            self.referal_code = self.generate_verification_code()
        return super(User, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
