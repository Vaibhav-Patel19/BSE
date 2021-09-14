from django.shortcuts import render
from .models import foodMenu, barMenu, foodOrder
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def homePage(request):

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
    all_drinktype = (
        ("1", "Beer"),
        ("2", "Cocktail"),
        ("3", "Gin"),
        ("4", "Red Wine"),
        ("5", "Sparkling Wine"),
        ("6", "Vodka"),
        ("7", "Whiskey"),
        ("8", "White Wine"),
    )

    #Newest Tab
    newest = foodMenu.objects.all().filter(newest=True)
    for i in newest:
        number = int(i.cuisine) - 1
        i.cuisine = all_cuisine[number][1]

    #recommended tab
    recommended = foodMenu.objects.all().filter(recommended=True)
    for i in recommended:
        number = int(i.cuisine)-1
        i.cuisine = all_cuisine[number][1]
    
    #recommended_Drink  
    recommended_drink = barMenu.objects.all().filter(recommended_drink=True)
    for i in recommended_drink:
        number = int(i.drinktype) - 1
        i.drinktype = all_drinktype[number][1]

    return render(request, "main/home.html", {"newest": newest, "recommended": recommended, "recommended_drink": recommended_drink})



def explorePage(request):

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

    all_drinktype = (
        ("1", "Beer"),
        ("2", "Cocktail"),
        ("3", "Gin"),
        ("4", "Red Wine"),
        ("5", "Sparkling Wine"),
        ("6", "Vodka"),
        ("7", "Whiskey"),
        ("8", "White Wine"),
    )

    #For diplaying different cuisines in explore page
    allcuisine = foodMenu.objects.order_by('cuisine').values('cuisine').distinct()
    for i in allcuisine:
        number = int(i['cuisine']) - 1
        i['cuisine'] = all_cuisine[number][1]


    #for displaying Drinktypes in Explore Page
    alldrinks = barMenu.objects.order_by('drinktype').values('drinktype').distinct()
    for i in alldrinks:
        number = int(i['drinktype']) - 1
        i['drinktype'] = all_drinktype[number][1]

    return render(request, "main/explore.html", {'allcuisine': allcuisine, 'alldrinks': alldrinks})


@cache_page(60 * 15)
@csrf_protect
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

    all_dish = foodMenu.objects.all().filter(cuisine__icontains = cuisine)


    #For Sending Order
    if request.method == "POST":
        dname = request.POST.get('dname', False)
        dqty = request.POST.get('dqty', False)
        dprice = request.POST.get('dprice', False)
        totamt = int(dprice) * int(dqty)

        order = foodOrder.objects.create(
            dishName = dname,
            price = totamt,
            quantity = dqty,
            cooked = False
        )

    return render(request, "main/menu.html",{'all_dish': all_dish, 'cuisine': cuisinename})



def showBarMenu(request, drinktype):

    all_drinktype = (
        ("1", "Beer"),
        ("2", "Cocktail"),
        ("3", "Gin"),
        ("4", "Red Wine"),
        ("5", "Sparkling Wine"),
        ("6", "Vodka"),
        ("7", "Whiskey"),
        ("8", "White Wine"),
    )

    for drink in all_drinktype:
        if drink[1] == drinktype:
            drinkname = drinktype
            drinktype = drink[0]
            break

    all_drinks = barMenu.objects.all().filter(drinktype__icontains = drinktype)


    return render(request, "main/barmenu.html",{'all_drinks': all_drinks, 'drinktype': drinktype, 'drinkname': drinkname})



def orderPage(request):
    return render(request, "main/order.html")
