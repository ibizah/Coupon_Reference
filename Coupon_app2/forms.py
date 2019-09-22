from django import forms
from . models import  User
from django.forms import ModelForm
from django.core import validators

class FormName(forms.Form):
    name= forms.CharField(label='Full Name :')
    email= forms.EmailField(label='Email :')
    text= forms.CharField(widget=forms.Textarea)

class UserForm(forms.ModelForm):
    alphanumeric =validators.RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    #first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z0-9]+', 'title':'Enter Alphanumeric Characters Only '}))
    name= forms.CharField()
    email= forms.EmailField()
    age= forms.IntegerField()
    city= forms.CharField()
    referal_code = forms.CharField(required=False, validators=[alphanumeric, validators.MaxLengthValidator(7)],widget=forms.TextInput(attrs={  'autocomplete': 'off','pattern':'[A-Za-z0-9]+', 'title':'Enter Alphanumeric Characters Only ','size':10}))

    class Meta:
        model= User
        fields= '__all__'
