from django.urls import path
from user.views import*

app_name = 'user'  

urlpatterns = [
    path('signin/', signin ,name='singin'),
    path('otvet/', signinotvet ,name='signinotvet'),
]