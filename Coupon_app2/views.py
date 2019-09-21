from django.shortcuts import render

from . forms import UserForm
# Create your views here.

def details(request):
    return render(request, 'details.html', name='details')
    
def form(request):
    form1 =UserForm()
    if request.method == 'POST':

        form1 = UserForm(request.POST)
        if form1.is_valid :
            form1.save(commit=True)
    return render(request, 'form.html',{'form1':form1, })
