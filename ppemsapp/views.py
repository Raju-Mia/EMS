from django.shortcuts import render
from .forms import *

# Create your views here.


def add_employee(request):
    if request.method == 'POST':
        pass
    else:
        form = UserForm()
        context = {'form':form}
        return render(request, 'ppemsapp/user_creation_form.html', context)
