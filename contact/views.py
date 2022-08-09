

from django.shortcuts import render, redirect
from django.urls import reverse
#importamos el modulo donde esta la clase ContactForm
from .forms import ContactoForm

from .models import Contact
from django.contrib.auth.decorators import login_required

#usamos el decorador
@login_required
def contact(request):
    contact_form = ContactoForm
    #validamos que ocurrio una peticion POST
    if request.method == "POST":
        #Traemos los datos enviados
        contact_form = contact_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if contact_form.is_valid():
            nameReceived = request.POST.get('name','')
            emailReceived = request.POST.get('email','')
            contentReceived = request.POST.get('content','')
            date = request.POST.get('date','')
            proyecto_id= request.POST.get('proyecto_id','')

            contacto = Contact(name=nameReceived,email=emailReceived,content=contentReceived,date=date, project=str(proyecto_id))
            contacto.save()

            return render(request,'contact/contact.html',{'enviado': nameReceived})   
    return render(request,'contact/contact.html',{'form': contact_form})



