from django.db import IntegrityError
from products.models import *
from django.views.generic import TemplateView , ListView
from django.shortcuts import render , redirect

class HeartView(ListView):
    template_name = "heart.html"
    model = Myheart
    context_object_name = 'heartlist'

    def get_queryset(self):
        return Myheart.objects.filter(user = self.request.user)
    
    
def add_to_whishlit(request,   product_pk):
    product = ProductModel.objects.get(pk=product_pk) 
    current_url_path = request.META.get('HTTP_REFERER')
    try:
        Myheart.objects.create(user=request.user, product=product)
    except IntegrityError:
        Myheart.objects.get(user=request.user, product=product).delete()
        
    return redirect(current_url_path)
        
