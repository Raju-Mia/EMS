from django.urls import path

from .views import *


urlpatterns = [
    path('add-employee/', add_employee, name='add-employee'),
    path('login/', user_login, name='user-login'),
]
