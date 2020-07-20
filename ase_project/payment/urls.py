from . import views
from django.urls import path

app_name = 'payment'

urlpatterns=[
    path('payment/process/',views.payment_process,name='process'), 
]