from django import forms
from . models import User
from django.forms import ModelForm

class FormName(forms.Form):
    name= forms.CharField(label='Full Name :')
    email= forms.EmailField(label='Email :')
    text= forms.CharField(widget=forms.Textarea)

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields= '__all__'
