from django.views.generic import TemplateView , ListView
from django.shortcuts import render
from pages.models import *
from products.models import ColorModel, ProductModel


class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class BlogPageView(TemplateView):
    template_name = 'blog.html'
    
class BlogDetailsView(TemplateView):
    template_name = 'blog-details.html'
    
class CheckoutPageView(TemplateView):
    template_name = 'checkout.html'
    
class ContactPageView(TemplateView):
    template_name = 'contact.html' 
    
    
class ShopPageView(ListView):
    template_name = 'shop.html'
    model = ProductModel
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Здесь добавляем данные о цветах товаров в контекст шаблона
        context['colors'] = ColorModel.objects.all()  # Предполагается, что у вас есть модель ColorModel для цветов товаров
        return context
    
class ShopDetailsView(TemplateView):
    template_name = 'shop-details.html'
    
        
class ShopCartView(TemplateView):
    template_name = 'shopping-cart.html'
    

    
class HomePageListView(ListView):
    model = MainCarusel
    template_name = 'home.html'
    # context_object_name = 'scrolls' 
    
    def get_queryset(self):     
        return MainCarusel.objects.filter(is_active=True)