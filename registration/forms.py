from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User #User Models in Database

class CreateUserForm(UserCreationForm):
    # class Meta to modify the Model
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']