from django.shortcuts import render
# Create your views here.
from django.shortcuts import HttpResponse



#app_prueba/views.py
def home(request):
    if request.user.username:
        return render(request,"app_prueba/home.html", {'name' : request.user.username})
    else:    
        return render(request,"app_prueba/home.html")


from .forms import FiltroParticipantes

from .models import Participantes
def about(request):
    nosotros = Participantes.objects.using('old').all() 
    filtro_form = FiltroParticipantes
    return render(request, "app_prueba/about.html", {'participantes': nosotros, 'form': filtro_form })




from .forms import FiltroParticipantes
from .models import Participantes

def about(request):
    nosotros = Participantes.objects.using('old').all() 
    filtro_form = FiltroParticipantes
    if request.method == "POST":
        filtro_form = filtro_form(data=request.POST)
        
        contiene = request.POST.get('name','')
        
        
        team = request.POST.get('team','')
        proyecto_id = request.POST.get('proyecto_id','')
        
        if team =='0':
            if proyecto_id =='0':
                nosotros = Participantes.objects.using('old').filter(name__contains=contiene).order_by('name')

            else:
                nosotros = Participantes.objects.using('old').filter(proyect_id=proyecto_id).filter(name__contains=contiene).order_by('name')

        else:
            nosotros = Participantes.objects.using('old').filter(proyect_id=proyecto_id).filter(team=team).filter(name__contains=contiene).order_by('name')  
        return render(request, "app_prueba/about.html", {'participantes': nosotros , 'form': filtro_form})
    return render(request, "app_prueba/about.html", {'participantes': nosotros , 'form': filtro_form})











#app_prueba/views.py
from django.shortcuts import render,redirect
from django.urls import reverse
# el form del registro
from .forms import RegistroForm
#para crear usuarios
from django.contrib.auth.models import User

def registro(request):
    registro_form = RegistroForm

    if request.method == "POST":
        #Traemos los datos enviados
        registro_form = registro_form(data=request.POST)
        #Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        #if registro_form.is_valid():
        cliente_id= request.POST.get('cliente_id','')
        email = request.POST.get('email','')
        pwd = request.POST.get('pwd','')

        user = User.objects.create_user(cliente_id, email, pwd)

        user.save()

        #En lugar de renderizar el template de prestamoo hacemos un redireccionamiento enviando una variable OK
        return redirect(reverse('login'))
    return render(request,"app_prueba/registro.html",{'form': registro_form})