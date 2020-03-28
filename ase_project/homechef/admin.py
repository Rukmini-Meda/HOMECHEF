from django.contrib import admin

# Register your models here.
from .models import Vendor, FoodItem, Ingredients
admin.site.register(Vendor)
admin.site.register(FoodItem)
admin.site.register(Ingredients)


