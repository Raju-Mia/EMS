from django.shortcuts import render, HttpResponse

from django.contrib.auth import authenticate, login

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
            login(request, user)
            return HttpResponse("Loged In")
    
    form = UserLogin()
    context ={ 'form':form }
    return render(request, 'ppemsapp/login.html', context)



# add daily report
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


# Leave application
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


# leave application query
def applications(request):
    try:
        applications = Leave.objects.filter(checked_in=False)
        if applications:
            context = {'applications': applications}
            return render(request, 'ppemsapp/applications.html', context)
        
        else:
            errormessage = "Here, is not available leave application"
            context = {'errormessage': errormessage}
            return render(request, 'ppemsapp/applications.html', context)
        
    except:
        pass


# leave appliation status and checked_in aprove.
def application_evaluation(request, status, id):
    application = Leave.objects.get(id=id)
    application.status = status
    print(status)
    application.checked_in = 1
    application.save()
    return HttpResponse("Leave application Accept")


# Leave application report for every users
def my_leave_report(request):
    try:
        
        my_application = Leave.objects.filter(user = request.user)
        if my_application:

            context = {'my_application': my_application}
            return render(request, 'ppemsapp/my_applications.html', context)
        else:
            report_errormessage = "YOU have no Leave applicatons"
            context = {'report_errormessage': report_errormessage}
            return render(request, 'ppemsapp/my_applications.html', context)

    except:
        pass