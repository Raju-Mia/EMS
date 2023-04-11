from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .forms import *

# Create your views here.


def home(request):
    return render(request, 'base/base.html')

@login_required(login_url='/login')
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
            return redirect('home')
    
    form = UserLogin()
    context ={ 'form':form }
    return render(request, 'ppemsapp/login.html', context)

#user logout
@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return redirect('/login')


# add daily report
@login_required(login_url='/login')
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
@login_required(login_url='/login')
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
@login_required(login_url='/login')
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
        
    except Exception:
        return redirect("login")


# leave appliation status and checked_in aprove.
@login_required(login_url='/login')
def application_evaluation(request, status, id):
    application = Leave.objects.get(id=id)
    application.status = status
    print(status)
    application.checked_in = 1
    application.save()
    return HttpResponse("Leave application Accept")


# Leave application report for every users
@login_required(login_url='/login')
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
        return redirect("login")

# My Todo List
@login_required(login_url='/login')
def my_todo_list(request):
    user = request.user
    pending_todo_list= TodoList.objects.filter(user=user, pending_status=True)
    working_status_list= TodoList.objects.filter(user=user, working_status=True)
    done_status_list= TodoList.objects.filter(user=user, done_status=True)
    context = {'pending_todo_list':pending_todo_list, 'working_status_list':working_status_list, 'done_status_list':done_status_list }
    return render(request, 'ppemsapp/my_todo_list.html', context)

# Action about Toto List Activites
@login_required(login_url='/login')
def action_todo_list(request,id,status):
    todo_list = TodoList.objects.get(id=id)
    if status == 'done':
        todo_list.pending_status = False
        todo_list.working_status = False
        todo_list.done_status = True
        todo_list.save()
        return redirect('my_todo_list')

    elif status == 'working':
        todo_list.working_status = True
        todo_list.pending_status = False
        todo_list.done_status = False
        todo_list.save()
        return redirect('my_todo_list')
    else:
        pass

# Create lodo list
@login_required(login_url='/login')
def add_todo_list(request):

    if request.method == 'POST':
        what_todo = request.POST['what_todo']
        when_todo = request.POST['when_todo']
        create_todo_list = TodoList.objects.create(user = request.user, what_to_do=what_todo, when_to_do=when_todo)
        return redirect('my_todo_list')
    else:
        pass


# user profile
@login_required(login_url='/login')
def profile(request):
    try:
        user = request.user
        print(user)
        if user:
            profile = Profile.objects.get(user=user)
            context ={'profile':profile}
            return render(request, 'ppemsapp/profile.html', context)
    except:
        messages = "user is not login"
        context = {'messages':messages}
        return render(request, 'ppemsapp/profile.html', context)