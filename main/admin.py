from django.contrib import admin
from .models import foodMenu, barMenu, foodOrder, barOrder

# Register your models here.


admin.site.register(foodMenu)
admin.site.register(barMenu)
admin.site.register(foodOrder)
admin.site.register(barOrder)