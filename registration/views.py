from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .forms import CreateUserForm # imoported from forms.py
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from main.models import foodOrder, barOrder
from payments.models import Payment

def landingPage(request):
    return render(request, 'landing/landing.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your account has been created!')

            return redirect('/login')

    context = {'form':form}
    return render(request, "registration/index.html", context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, "registration/login.html", context)


def logoutUser(request):

    Payment.objects.all().filter(user = request.user).update(bill_paid = True)

    foodOrder.objects.all().filter(user = request.user).delete()

    barOrder.objects.all().filter(user = request.user).delete()

    logout(request)
    return redirect('/login')
