from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.landing, name = 'landing'),
    path('vendor/<vendor_id>',views.display,name="display"),
    path('product/<vendor_id>/<food_id>',views.product,name="product"),
    path('search/',views.search,name="search"),
    path('food/<food_id>',views.vendorlist,name="vendorlist"),
    path('add-to-cart/<vendor_id>/<food_id>/',views.add_to_cart,name="add-to-cart"),
    path('remove-from-cart/<vendor_id>/<food_id>/',views.remove_from_cart,name="remove-from-cart"),
    path('remove-single-item-from-cart/<vendor_id>/<food_id>/',views.remove_single_item_from_cart,name="remove-single-item-from-cart"),
    path('order-summary/',views.OrderSummaryView.as_view(),name="order-summary"),
    path('checkout/',views.CheckoutView.as_view(),name="checkout"),
    path('bevolunteer/',views.Bevolunteer,name="bevolunteer"),
    path('Volunteerform/',views.Volunteerform,name="Volunteerform"),
    path('selling1/',views.Selling1,name="selling1"),
    path('payment/process/',views.payment_process,name='process'), 
]