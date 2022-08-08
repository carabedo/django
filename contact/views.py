

from django.shortcuts import render, redirect
from django.urls import reverse
#importamos el modulo donde esta la clase ContactForm
from .forms import ContactoForm

def contact(request):
    contact_form = ContactoForm
    #validamos que ocurrio una peticion POST
    if request.method == "POST":
        #Traemos los datos enviados
        contact_form = contact_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if contact_form.is_valid():
            name = request.POST.get('name','Tu nombre')
            return render(request,'contact/contact.html',{'enviado': name})         
    return render(request,'contact/contact.html',{'form': contact_form})