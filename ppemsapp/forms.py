from django import forms
from django.contrib.auth.models import Group, User
from. models import *

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-field form-control bg-light'}))
    roll = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control bg-light'}), queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'roll', 'password']

        help_texts = {
            'username':None,
            'email':None
        }

        widgets = {

            'first_name' : forms.TextInput(attrs={'class':'form-control bg-light'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control bg-light'}),
            'email' : forms.TextInput(attrs={'class':'form-control bg-light'}),
            'username' : forms.TextInput(attrs={'class':'form-control bg-light'}),
        }
    
    


# userlogin form
class UserLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-field form-control', 'placeholder':'Inter your username..'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-field form-control bg-light', 'placeholder':'Inter your password..'}))




# Daily TaskForm
class DailyTaskForm(forms.ModelForm):
    class Meta:
        model = DailyTask

        fields = '__all__'

        exclude = ['date', 'user']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'discription':forms.Textarea(attrs={'class':'form-control'})
        }


#Leave
class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        # exclude = ['user', 'status', 'checked_in']

        fields = ['cause_of_leave', 'from_date', 'to_date']

        widgets = {
            
            'from_date':forms.DateInput(attrs={'type':'date', 'class':'form-control datepicker'}),
            'to_date':forms.DateInput(attrs={'type':'date', 'class':'form-control datepicker'}),
            'cause_of_leave':forms.Textarea(attrs={'class':'form-control'})
        }
