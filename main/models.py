from django.db import models
# from django.contrib.auth import get_user_model

# Create your models here.

# User = get_user_model()

class foodMenu(models.Model):
    foodtype = (
        ("1", "Veg"),
        ("2", "Non-Veg"),
    )

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


    foodtype = models.CharField(choices=foodtype, max_length=10)
    cuisine = models.CharField(choices=all_cuisine, max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(null=True)
    newest = models.BooleanField(default=False)
    recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.get_cuisine_display() + " - " + self.name

    class Meta:
        verbose_name_plural = "Food Menu"



class barMenu(models.Model):

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

    drinktype = models.CharField(choices=all_drinktype, max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)

    actual_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    current_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    total_qty = models.IntegerField(null=True)
    savings = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    low = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    high = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    className = models.CharField(max_length=50, blank=True)
    recommended_drink = models.BooleanField(default=False)

    def __str__(self):
        return self.get_drinktype_display() + " - " + self.name

    class Meta:
        verbose_name_plural = "Bar Menu"


class foodOrder(models.Model):

    dishName = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    quantity = models.IntegerField(null=True)
    cooked = models.BooleanField(default=False)

    def __str__(self):
        return self.dishName

    class Meta:
        verbose_name_plural = "Ordered Food"    
        # This class will add a title in DB.
    