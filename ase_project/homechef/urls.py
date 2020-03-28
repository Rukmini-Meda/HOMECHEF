from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name = 'landing'),
    path('vendor/<vendor_id>',views.display,name="display"),
    path('vendor/<vendor_id>/<food_id>',views.product,name="product"),
    path('food/<vendor_id>/<food_id>',views.product,name="product"),
    path('search/',views.search,name="search"),
    path('food/<food_id>',views.vendorlist,name="vendorlist")
]