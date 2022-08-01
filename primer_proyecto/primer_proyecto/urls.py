"""primer_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_prueba import views as views_app_prueba


urlpatterns = [
    path('',views_app_prueba.home, name="home"), 
    path('contact/',views_app_prueba.contact, name="contact"), 
    path('about/',views_app_prueba.about, name="about"), 
    path('portfolio/',views_app_prueba.portfolio, name="portfolio"), 
    path('admin/', admin.site.urls),
]
