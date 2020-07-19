from django import template
from homechef.models import Order

register = template.Library()

@register.filter
def cart_items_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user,ordered=False)
        if qs.exists():
            return qs[0].items.count()
        else:
            return 0