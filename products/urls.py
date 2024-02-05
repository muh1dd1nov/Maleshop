from django.urls import path
from products.views import*

app_name = 'products'  

urlpatterns = [
    path('myheart/', HeartView.as_view() ,name='heart'),
    path('<int:product_pk>/addtoheart/',add_to_whishlit,name = 'add_to_whishlist')
]