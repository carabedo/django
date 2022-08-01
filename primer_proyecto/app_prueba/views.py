from django.shortcuts import render
# Create your views here.
from django.shortcuts import HttpResponse



#app_prueba/views.py
def home(request):
    return render(request, "app_prueba/home.html") 

def contact(request):
    return render(request, "app_prueba/contact.html") 

def about(request):
    return render(request, "app_prueba/about.html") 

def portfolio(request):
    return render(request, "app_prueba/portfolio.html") 