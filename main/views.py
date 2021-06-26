from django.shortcuts import render
from .models import foodMenu

# Create your views here.

def homePage(request):
    return render(request, "main/home.html")

def explorePage(request):
    return render(request, "main/explore.html")

def orderPage(request):
    return render(request, "main/order.html")


def showMenu(request, cuisine):
    all_cuisine = (
        ("1", "Soup"),
        ("2", "Salad"),
        ("3", "Appetizers"),
        ("4", "Italian Mainfare"),
        ("5", "Mexican Mainfare"),
        ("6", "Pastas"),
        ("7", "Pizzas"),
        ("8", "Rice"),
        ("9", "Fondue"),
        ("10", "Desserts"),
    )

    for c in all_cuisine:
        if c[1] == cuisine:
            cuisinename = cuisine
            cuisine = c[0]
            break

    all_dish = foodMenu.objects.all().filter(cuisine__icontains=cuisine)

    return render(request, "main/menu.html")
