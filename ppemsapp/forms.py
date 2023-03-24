from django import forms
from django.contrib.auth.models import Group, User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control bg-light'}))
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
    
    