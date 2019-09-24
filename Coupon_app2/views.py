from django.shortcuts import render

from . forms import UserForm
from .models import User
# Create your views here.
import datetime
from django.core.mail import send_mail


def details(request):
    user_data= User.objects.all()
    dic={'user_records':user_data}

    return render(request, 'details.html',dic)

def form(request):
    x = datetime.datetime.now()
    dic={'date':x.year}
    form1 =UserForm()
    form1 = UserForm(request.POST)
    if request.method == 'POST' and  form1.is_valid():

            # fn=form1.cleaned_data['name']
            # mail=form1.cleaned_data['email']
            # age=form1.cleaned_data['age']
            #dic={'fn':fn,'mail':mail,'age':age}
            #print(f'your name is {dic["fn"]},email is  {dic["mail"]}')
            form1.save(commit=True)
    return render(request, 'form.html',{'form1':form1,})
