from django.urls import path

from pages.views import *
app_name = 'pages'

urlpatterns = [
    path('', HomePageListView.as_view() ,name='home'),
    path('shop/', ShopPageView.as_view(), name='shop'),
    path('shop_details/',ShopDetailsView.as_view(),name='shop_details'),
    path('shopping_cart/',ShopCartView.as_view(),name='shop_cart'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog_details/', BlogDetailsView.as_view(), name='blog_details'),
    path('blog/', BlogPageView.as_view(),name='blog'),
    path('checkout/', CheckoutPageView.as_view(),name = 'checkout'),
    path('contact/', ContactPageView.as_view(),name='contact'),
]   