from django.db import models
from django.forms import ModelForm
from django.core import validators
import string, random


# Create your models here.

class User(models.Model):
    alphanumeric =validators.RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    name= models.CharField(max_length=200)
    email= models.EmailField(max_length=100)
    age= models.IntegerField()
    city= models.CharField(max_length=100)
    referal_code = models.CharField(max_length=7, blank=True, null=True, unique=True, validators=[alphanumeric])


    def generate_verification_code(self):
        newreferal_code = ''.join([''.join(random.sample(string.ascii_letters, 2)),''.join(random.sample(string.digits, 3)),''.join(random.sample(string.ascii_letters, 2))])
        newreferal_code = list(newreferal_code)
        random.shuffle(newreferal_code)
        newreferal_code =''.join(newreferal_code)
        return newreferal_code


    def save(self, *args, **kwargs):
        if not self.pk:
            self.referal_code = self.generate_verification_code()
        if not self.referal_code:
            self.referal_code = self.generate_verification_code()
        return super(User, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
