from django.shortcuts import render

def signin(request):
    return render(request,template_name='user_index.html')

def signinotvet(request):
    return render(request,template_name='main.html')