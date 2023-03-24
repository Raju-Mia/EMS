from django.urls import path

from .views import *


urlpatterns = [
    path('add-employee/', add_employee, name='add-employee'),
]
