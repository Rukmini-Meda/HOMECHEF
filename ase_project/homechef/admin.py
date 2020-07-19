from django.contrib import admin

# Register your models here.
from .models import Vendor, FoodItem, Ingredients, OrderItem, Order
admin.site.register(Vendor)
admin.site.register(FoodItem)
admin.site.register(Ingredients)
admin.site.register(OrderItem)
admin.site.register(Order)

