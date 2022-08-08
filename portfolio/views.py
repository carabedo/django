from django.shortcuts import render

from .models import Proyectos

# Create your views here.
from django.contrib.auth.decorators import login_required

#usamos el decorador
@login_required
def portfolio(request):
    projects = Proyectos.objects.all() 
    return render(request, "portfolio/portfolio.html", {'projects': projects })
