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