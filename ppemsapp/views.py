from django.shortcuts import render, HttpResponse

from django.contrib.auth import authenticate

from .forms import *

# Create your views here.


def home(request):
    return render(request, 'base/base.html')


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
            UserLogin(request, user)
            return HttpResponse("Loged In")
    
    form = UserLogin()
    context ={ 'form':form }
    return render(request, 'ppemsapp/login.html', context)




def add_daily_report(request):

    if request.method == 'POST':
        form = DailyTaskForm(request.POST)
        if form.is_valid():
            form =form.save(commit=False)
            user = request.user
            form.user = user
            form.save()
            return HttpResponse("Dailly Task submit successfully")


    form = DailyTaskForm()
    context = {'form':form}
    return render(request, 'ppemsapp/add-task.html', context)


def leave(request):

    if request.method == 'POST':
        form = LeaveForm(request.POST)

        if form.is_valid():
            form =form.save(commit = False)

            form.user = request.user
            form.save()

            return HttpResponse("leave apply success")
        

    form = LeaveForm()
    context = {'form':form}
    return render(request, 'ppemsapp/add-leave.html', context)