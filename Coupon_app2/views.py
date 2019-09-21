from django.shortcuts import render

from . forms import UserForm
from .models import User
# Create your views here.
import datetime


def details(request):
    user_data= User.objects.all()
    dic={'user_records':user_data}
    
    return render(request, 'details.html',dic)

def form(request):
    x = datetime.datetime.now()
    dic={'date':x.year}
    form1 =UserForm()
    if request.method == 'POST':

        form1 = UserForm(request.POST)
        if form1.is_valid :
            form1.save(commit=True)
    return render(request, 'form.html',{'form1':form1,},dic)
