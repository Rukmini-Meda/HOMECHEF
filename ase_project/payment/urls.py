from django.conf.urls import url
from . import views

app_name = 'payment'

urlpatterns=[
    url(r'^process/$',views.payment_process,name='process'),
   
]