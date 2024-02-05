from django import template

from products.models import Myheart

register = template.Library()

@register.filter(name='in_whishlist')
def in_whishlist(user,product):
    return Myheart.objects.filter(user=user,product=product).exists()
    