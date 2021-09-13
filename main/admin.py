from django.contrib import admin
from .models import foodMenu, barMenu, foodOrder

# Register your models here.


admin.site.register(foodMenu)
admin.site.register(barMenu)
admin.site.register(foodOrder)
