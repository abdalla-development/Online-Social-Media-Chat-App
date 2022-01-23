from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField() 
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', "password2" , "first_name", "last_name"]  
