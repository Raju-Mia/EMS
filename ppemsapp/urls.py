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
]
