from django.urls import path

from .views import *


urlpatterns = [
    path('add-employee/', add_employee, name='add-employee'),
    path('login/', user_login, name='user-login'),
    path('add-daily-task/', add_daily_report, name='add-daily-report'),
    path('', home, name='home'),
    path('leave/', leave , name='leave'),
    path('applications/', applications, name='applications'),
    path('application_evaluation/<status>/<id>/', application_evaluation, name='application-evaluation'),
    path('my_application/', my_leave_report, name='my-leave-report'),
    path('todo-list/', my_todo_list, name='my_todo_list'),
    path('action-todo-list/<id>/<status>', action_todo_list, name="action_todo_list"),
    path('add-todo-list/', add_todo_list, name="add_todo_list"),
    path('profile/', profile, name="profile"),
]
