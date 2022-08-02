from django.shortcuts import render

from .models import Proyectos

# Create your views here.


def portfolio(request):
    projects = Proyectos.objects.all() 
    return render(request, "portfolio/portfolio.html", {'projects': projects })
