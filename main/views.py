from django.shortcuts import render
# Create your views here.

def homePage(request):
    return render(request, "main/home.html")

def explorePage(request):
    return render(request, "main/explore.html")

def orderPage(request):
    return render(request, "main/order.html")
