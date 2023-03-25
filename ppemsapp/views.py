from django.shortcuts import render, HttpResponse

from django.contrib.auth import authenticate
from .forms import *

# Create your views here.


def add_employee(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Form submit successfully")
        
    else:
        form = UserForm()
        context = {'form':form}
        return render(request, 'ppemsapp/user_creation_form.html', context)


#UserLogin 
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        print("data not vaild")
        if user:
            login(request, user)
            return HttpResponse("Loged In")
    
    form = UserLogin()
    context ={ 'form':form }
    return render(request, 'ppemsapp/login.html', context)