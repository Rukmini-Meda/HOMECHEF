from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from homechef import models

def payment_process(request):
    # What you want the button to do.
    order = models.Order.objects.get(user=request.user,ordered=False)
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL, #Here you can change the email.
        "amount": order.get_order_total(),
        "item_name":'Give item name',
        "invoice":'The invoice you wanted to give',
        "currency_code": 'INR',
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }
    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        'form': form,
        'data': order
    }
    return render(request, "payment/payment.html", context)
