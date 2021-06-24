from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')

    context = {'form':form}
    return render(request, "registration/index.html", context)

def loginPage(request):
    return render(request, "registration/login.html")
