# DJANGO
- [Apps](https://github.com/carabedo/django/blob/main/README.md#creemos-nuestra-primer-app)
- [Static Files](https://github.com/carabedo/django#static-files-models-admin)
- [Models](https://github.com/carabedo/django#models)
- [Admin](https://github.com/carabedo/django#admin)
- [MVT](https://github.com/carabedo/django#mvt)
- [Forms](https://github.com/carabedo/django#formularios)
- [Sesiones](https://github.com/carabedo/django#sesiones)
- [Autentificaciones](https://github.com/carabedo/django#autentificaciones)
- [Registro Usuarios](https://github.com/carabedo/django#registracion)
- [Importando DB](https://github.com/carabedo/django#importando-dbs)
- [Queries](https://github.com/carabedo/django#queries)
- [Seguridad](https://github.com/carabedo/django#seguridad)

## Instalacion UNIX (linux/macos)



```bash
pip3 install django
``` 

## Instalacion Windows

Tenemos dos opciones:

### Linux en windows

Luego de instalar linux
https://docs.microsoft.com/en-us/windows/wsl/install

```bash
pip3 install django
``` 
Por ultimo instalamos la extension de VScode que nos permite trabajar desde linux.

https://code.visualstudio.com/docs/remote/wsl

### Miniconda

https://docs.conda.io/en/latest/miniconda.html

Luego de instalar miniconda, ejecutar desde la `anaconda prompt`


```bash
conda install django
``` 

VScode automaticamente va a detectar esta instalacion de python, pero no la usara por default si hay otras instalaciones existentes, debemos setearlo.


----

## Creamos nuestro `primer_proyecto`!

```bash
django-admin startproject primer_proyecto
```

Deberiamos observar que se creo la siguiente estructura de carpetas y archivos:

```
primer_proyecto/
├─ manage.py
├─ primer_proyecto/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py

````


Ahora vamos levantar nuestro servidor, para eso nos metemos en la carpeta creada por el `django-admin`.
```bash
cd primer_proyecto
```
Y por ultimo ejecutar la siguiente linea:


```bash
python3 manage.py runserver
```

Si todo funciono bien, deberiamos ver nuestro proyecto en http://127.0.0.1:8000/

Ahora migremos los datos del proyecto a la base de datos:

```bash
python3 manage.py migrate
```
Podemos ver que ahora la base de datos tiene varias tablas.

## Creemos nuestra primer APP!

Podemos decir que una app es una aplicación web que implementa una funcionalidad y un proyecto es un conjunto de
configuraciones a las que se "conectan" esas apps para que todo unido de lugar a un sitio web completo. 
Un proyecto puede contener múltiples apps y una app puede ser incluida en múltiples proyectos.

Una app no es simplemente una pagina.

```bash
python3 manage.py startapp app_prueba
```

Deberiamos observar que se creo la siguiente estructura de carpetas y archivos:

```
primer_proyecto/
├─ manage.py
├─ app_prueba/
│  ├─ __init__.py
│  ├─ views.py
│  ├─ tests.py
│  ├─ models.py
│  ├─ apps.py
│  ├─ admin.py
│  ├─ migrations/
├─ primer_proyecto/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py

````

Vemos que dentro de nuestra aplicación `app_prueba`, vamos a encontrar varios archivos:

- views.py: Una vista hace referencia a la lógica que se ejecuta cuando se hace una
petición a nuestra web.


Vamos a editar `views.py` para crear nuestra primera vista:


```python
#app_prueba/views.py
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenidxs a mi primer sitio hecho con DJANGO!</h1>")

```

Ahora vamos a editar el fichero mapeador de URLs (urls.py) en la carpeta
del proyecto. Aunque puedes usar este fichero para gestionar todos tus
mapeos URL, es más usual deferir los mapeos a su aplicación asociada.


```python
##primer_proyecto/urls.py

#del modulo app_prueba (fijarse que tiene __init.py__) importamos el módulo views
#es decir, de la app prueba importamos las vistas. 
from app_prueba import views

urlpatterns = [
    #Creamos un patrón url, en la raíz del sitio (cadena vacía) desde el que llamaremos 
    # a la vista views.home que tiene el nombre home.
    path('',views.home, name="home"), 
    path('admin/', admin.site.urls),
]
``` 

Ahora deberiamos ver nuestro HOME.


## Usando el back en el front:

Definamos una vista un poco mas compleja:

```python
#app_prueba/views.py
from django.shortcuts import HttpResponse

def home(request):
    html_response = "<h1>Bienvenidxs a mi primer sitio hecho con DJANGO!</h1>"
    for i in range(10):
        html_response += "<p>Línea " + str(i) + "</p>"
    return HttpResponse(html_response)
```

### Templates:

Por algo estuvimos varias semanas aprendiendo html css js, reutilicemos lo que ya hicimos!
Para utilizar una plantilla necesitamos crearla. Lo primero es crear una
carpeta `templates` en nuestra app `app_prueba`, que dentro debe contener otra carpeta
con el mismo nombre que la app, en nuestro caso prueba `app_prueba`.

```bash
cd app_prueba
mkdir templates
cd templates
mkdir app_prueba
touch home.html
```

Con estas lineas creamos todo lo necesario, ahora podemos editar el `home.html`.



Ahora tenemos que cambiar nuestra vista para que en lugar de devolver la
respuesta HttpResponse devuelva el template HTML utilizando el método
render del módulo http de Django, que ya viene incluido por defecto.

Primer tenemos que registrar la app `app_prueba` en el archivo `settings.py`.
Por defecto Django optimiza el uso de la memoria así que no carga las plantillas de una app que no esté instalada en settings.py.

```python
##primer_proyecto/settings.py deberia quedar asi:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_prueba'
]
``` 

Redefinamos nuestra vista:


```python
#app_prueba/views.py
def home(request):
    return render(request, "app_prueba/home.html") 
```

### Herencia de templates:

Generemos esta templates `base.html` en `app_prueba/templates/app_prueba/`: 

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sitio Web de Prueba</title>
</head>
<body>
<h1>Bienvenido a mi sitio web de Prueba</h1>
<ul>
<li><a href="/">Home</a></li>
<li><a href="/about/">Quienes somos</a></li>
<li><a href="/portfolio/">Proyectos</a></li>
<li><a href="/contact/">Contacto</a></li>
</ul>
<!-- Ahora viene la parte que vamos a cambiar en cada página-->
{% block content %}
{% endblock %}

<!-- Usamos un template tag BLOCK, una etiqueta de template,sirve para
añadir lógica de programación dentro del propio HTML -->
</body>
</html>
```

Un template tag, una etiqueta de template, sirve para añadir lógica de
programación dentro del propio HTML. Existen muchos template tags en
Django.

https://www.w3schools.com/django/django_template_tags.php

#### Template tag: BLOCK


Ahora modificamos el archivo `home.html`:

```html
!-- agregamos el bloque extends que tomara el html base-->
{% extends 'prueba/base.html' %}
<!-- indicamos que lo de abajao se dibuje despues del menu armado en la
base-->
{% block content %}
<h1>Bienvenidxs al home</h1>
<h2>Este es el home.</h2>
<p>FS 2022</p>
{% endblock %}
```

#### Template tag: URL

```python
{% url %}
```

Este tag nos permite hacer referencia directamente a una view desde
nuestros templates y es la forma correcta de escribir enlaces relativos
dentro de nuestra web.

En el template `base.html` podemos sustituir los enlaces "hardcodeados" por url automatizadas.

```html
<li><a href="{% url 'home' %}">Inicio</a></li>
<li><a href="{% url 'about' %}">Acerca de</a></li>
<li><a href="{% url 'portfolio' %}">Portafolio</a></li>
<li><a href="{% url 'contact' %}">Contacto</a></li>
```

Es una buena práctica nunca utilizar hardcodeo para los enlaces, siempre
es mejor usar este tag.

# Static Files, Models, Admin.

## Uniendo el front con el back.

Es común en las organizaciones que el diseño de front-end se encargue a una empresa de diseño y el mismo sea suministrado al equipo de desarrollo para integrar con el backend de la empresa.

Cuando se fusiona un frontend existente con un backend hay que identificar los elementos comunes y dinámicos de las páginas para aplicar la lógica de la herencia de plantillas. Adicionalmente los sitios web se componen de recursos estáticos como css, javascript e imágenes.

Para poder ver estos recursos mientras desarrollamos nuestro sitio, tenemos que incorporarlos a nuestro directorio de templates.
Crearemos un directorio static y dentro otro llamado `app_prueba`, el nombre de la app, donde vamos a copiar todos los directorios de la maqueta que incluyen este tipo de archivos:


[Descargar](https://github.com/carabedo/labs/raw/master/data/static_c2.zip)

[Archivos](https://github.com/carabedo/fs-itba/tree/main/Sprint%207/Clase%202/UniendoFrontEndBackEnd/sitio_prueba/prueba/static/prueba)


Muy importante respetar esta estructura:

```
primer_proyecto/
├─ app_prueba/
│  ├─ static/
│  │  ├─ app_prueba/
│  │  │  ├─ css/
│  │  │  │  ├─ style.css
│  │  │  ├─ js/
│  │  │  │  ├─ main.js
│  │  │  ├─ imgs/
│  │  │  │  ├─ banner.png

```


### Template `base.html` 

Una vez que incorporamos los recursos estáticos tenemos que indicar al template `base.html` que necesitamos cargar los recursos estáticos, usando el template tag load.



```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Estilos y fuentes del template  -->
    {% load static %}
    <link href="{% static 'app_prueba/vendor/bootstrap/css/bootstrap.min.css' %}" rel="stylesheet">
    <link href="{% static 'app_prueba/vendor/font-awesome/css/font-awesome.min.css' %}" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>
    <!--Luego, identificamos el contenido dinámico y usaremos el template tag block-->
    <link href="{% static 'app_prueba/css/clean-blog.min.css' %}" rel="stylesheet">
    <title>{% block title %}{% endblock %} | ITBANLK Portfolio de Proyectos </title>
  </head>
```


Sigamos con el `body`:


Otro contenido dinámico que tenemos son los links a las distintas páginas, en este caso usamos el template tag url. 


```html
  <body>
  <!-- Navegación -->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
      <div class="container">
        <a class="navbar-brand" href="{% url 'home' %}"> Portafolio de proyectos</a>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" 
          data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
          aria-label="Toggle navigation">Menú<i class="fa fa-bars"></i></button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
          <li class="nav-item"><a class="nav-link" href="{% url 'home' %}">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="{% url 'about' %}">Quienes Somos</a></li>
          <li class="nav-item"><a class="nav-link" href="{% url 'portfolio' %}">Portafolio</a></li>
          <li class="nav-item"><a class="nav-link" href="{% url 'contact' %}">Contacto</a></li>
          </ul>
        </div>
       </div>
    </nav>
```
Notar que deben estar creadas las views y agragadas las url para (about,portfolio y contact).

Agregamos la imagen de fondo en la sección cabecera y los títulos de la sección:


```html
    <header class="masthead" style="background-image: url('{% block background %}{% endblock %}')">
      <div class="overlay"></div>
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-10 mx-auto">
            <div class="site-heading">
                {% block headers %}{% endblock %}
            </div>
          </div>
        </div>
      </div>
    </header>
```

Por ultimo agregamos el bloque de contenido, entre el header y el footer.

```html
    <!-- Contenido -->
        {% block content %}{% endblock %}
    <!-- Pié de página -->
    <footer>
    <div class="container"><div class="row"><div class="col-lg-8 col-md-10 mx-auto"><ul class="list-inline text-center"><li class="list-inline-item"><a href="#"><span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-envelope fa-stack-1x fa-inverse"></i></span></a></li><li class="list-inline-item"><a href="#"><span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-github fa-stack-1x fa-inverse"></i></span></a></li><li class="list-inline-item"><a href="#"><span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-youtube fa-stack-1x fa-inverse"></i></span></a></li></ul><p class="copyright text-muted">Copyright &copy; 2022</p></div></div></div></footer>
    <!-- Bootstrap y Javascripts -->
    <script src="{% static 'app_prueba/vendor/jquery/jquery.min.js' %}"></script>
    <script src="{% static 'app_prueba/vendor/bootstrap/js/bootstrap.bundle.min.js' %}"></script>
    <script src="{% static 'app_prueba/js/clean-blog.min.js' %}"></script>
  </body>
</html>
```

Una vez que trabajamos con nuestro template base, ahora modificamos el archivo de la `home`, para que herede las configuraciones de la plantilla base.

### Template `home.html` 

```html
<!-- agregamos el bloque extends que tomara el html base-->
{% extends 'app_prueba/base.html' %}
<!-- Agregamos el contenido estatico-->
{% load static %}
<!-- Agregamos el titulo de la home -->
{% block title %} Gestion de Proyectos - Inicio {% endblock %}
<!-- Agregamos la imagen de fondo -->
{% block background %}{% static 'app_prueba/img/home-bg.jpg' %}{% endblock %}
<!-- Agregamos la informacion que queremos en el header-->
{% block headers %}
    <h1>Sitio de Gestión de Proyectos</h1>
    <span class="subheading">Area de Tecnología de la Información</span>
{% endblock %}
<!-- indicamos que lo de abajao se dibuje despues del menu armado en la base-->
{% block content %}
{% endblock %}
```

# Models

Nuestro `primer_proyecto` es un ejemplo de un sitio de gestión de proyectos, por eso vamos a necesitar los campos: títulos, descripción, imagen y enlace.

Para tal fin, vamos a crear una nueva app, denominada portfolio:

```bash
python3 manage.py startapp portfolio
```

Una vez creada nuestra nueva app, vamos a definir un nuevo modelo `Proyectos`. Vamos a ir al archivo `portfolio/models.py`.
Para crear un modelo, tenemos que crear una clase heredando de una clase padre llamada `models.Model`.


Luego tenemos que crear sus columnas, que van a ser los atributos de la clase. Crearemos el título, la descripción, imagen y enlace, además de dos campos especiales que nos servirán para almacenar automáticamente la fecha y hora de creación del registro, así como la fecha y hora de la última edición. A cada uno de estos campos le tenemos que indicar el tipo de datos.

```python
##portfolio/models.py
#agregamos los atributos con el tipo de datos de Models
class Proyectos(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título") #agregamos el campo verbose para describir
    description =  models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='proyectos_imgs',verbose_name="Imagen",null=True, blank=True)
    #el atributo upload_to, permite idnicar donde subir las imagenes
    link = models.URLField(null=True, blank=True, verbose_name="Enlace Web")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

```

Existe varios tipos de datos, nosotros usamos texto corto, texto más largo, imagen y fecha.

Un listado completo [aca](https://docs.djangoproject.com/en/4.0/ref/models/fields/)

Una vez definido nuestro modelo, tenemos que agregar la app portfolio al proyecto (en el archivo settings):

```python
##primer_proyecto/settings.py
INSTALLED_APPS = [ 'django.contrib.admin', 
                    'django.contrib.auth', 
                    'django.contrib.contenttypes',
                    'django.contrib.sessions', 
                    'django.contrib.messages', 
                    'django.contrib.staticfiles', 
                    'app_prueba',
                    'portfolio']
```

Una vez configurada la app, tenemos que ejecutar la migración a la base de datos con dos comandos:

```bash
python3 manage.py makemigrations portfolio
python3 manage.py migrate portfolio 
```
Cada vez que hagamos un cambio en nuestro archivo models.py tenemos que ejecutar estos dos comandos para crear una migración y posteriormente aplicarla.

# Admin

Creemos el usuario admin:

```
python3 manage.py createsuperuser
```

Una vez creado el usuario tenemos que iniciar nuevamente el servidor, con el comando runserver, accediendo a la sección admin con el nuevo usuario creado, tendremos que ver la siguiente pantalla.

Al ingresar como super usuario podemos editar cualquier tabla de la base de datos a voluntad, aunque por ahora sólo nos aparecen las tablas de grupos y usuarios.

![](admin.png)

Todavía no se ve la tabla proyecto que creamos, porque no la registramos en el admin de nuestra app portfolio.



```python
##portfolio/admin.py
from .models import Proyectos
# Register your models here.
admin.site.register(Proyectos)
```


Una vez registrado `Proyectos`, actualizando el sitio de navegador vamos a encontrar la tabla proyectos que pertenece a la app portfolio.


![](admin2.png)


Haciendo clic en Añadir, podremos agregar un proyecto

### Customizando el admin panel:

Si la carga de datos al sitio web se realizara a través del panel administrador, es conveniente agregar más información para que su funcionamiento sea más sencillo.

#### verbose_name:

En el archivo apps.py, agregamos el nuevo nombre:

```python
##portfolio/apps.py
from django.apps import AppConfig
class PortfolioConfig(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField' name = 'portfolio'
  verbose_name = 'Portafolio'
```

Lo mismo podemos hacer en la clase `Proyectos` que definimos anteriormente, podemos cambiar los nombres de los campos, como queremos que se ordene la información, etc. En el archivo de modelos vamos a usar la subclase Meta y el método especial __str__.

Al crear la clase `Proyectos` hemos decidido ponerle Proyectos, pero en el panel vemos que le agrega una 's' podemos cambiar el nombre a mostrar en el panel de forma muy sencilla creando una subclase con Meta información, adicionalmente a cada campo le vamos agregar como parámetro el `verbose_name` y un campo de ordenación por defecto, en este caso la fecha de creación. 

Adicionalmente indicamos que los campos imagen y link, pueden tomar valores nulos.

```python
#agregamos los atributos con el tipo de datos de Models
class Proyectos(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    #agregamos el campo verbose para describir
    description =  models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='projects',verbose_name="Imagen",null=True, blank=True)
    #el atributo upload_to, permite idnicar donde subir las imagenes
    link = models.URLField(null=True, blank=True, verbose_name="Enlace Web")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    #creamos una subclase con Meta información:
    class Meta: 
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] #este campo indica que ordenemos los registros por fecha de creado en forma descendente
        
    # redefinimos el método especial __str__ para que devuelva la cadena que nosotros queramos, en vez del 'object' 
    def __str__(self): 
        return self.title
  
```

#### campos especiales:

Los campos de fecha y hora automatizados no aparecen en el administrador, Django no los muestra para que no se puedan modificar, pero podemos mostrarlos como campos de tipo "sólo lectura". Para hacerlo tenemos que extender un poco la configuración base del administrador de la siguiente forma:

```python
##portfolio/admin.py
from django.contrib import admin from .models import Project
# Register your models here.
#Con esta clase ampliamos la configuracion del administrador, extendiendo nuesrta clase propia
#Le decimos que los campos created y updated son de solo lectura
class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')
admin.site.register(Project)
```

#### media:

Los archivos que sube un usuario a través del administrador, no se consideran recursos estáticos, se denominan archivos multimedia
Para poder cargar y después referir archivos de este tipo, necesitamos crear una carpeta donde almacenar estos recursos. 

La llamamos media y la creamos en la raíz de nuestro proyecto:

```
primer_proyecto/
├─ primer_proyecto/
├─ portfolio/
├─ app_prueba/
├─ manage.py
├─ db.sqlite3
├─ media/
```


Luego en el archivo settings.py y abajo de todo añadimos dos variables, una para indicar la URL externa y otra para la carpeta interna donde se encuentran los archivos media.

```python
##settings.py
import os
# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

Si queremos ver la imagen en nuestro servidore de desarrollo, tenemos que editar nuestro archivo urls.py, en este caso se usara solo en modo debug

```python
##urls.py
from django.conf import settings
if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Como resultado, Podemos crear un proyecto en nuestra herramienta de gestión de portfolio de forma completa, modificarlo y visualizarlo.



# MVT

Integremos los modelos en las vitas, para eso vamos a importar el modelo `Proyectos` a la vista de portfolio:


```python
##portfolio/views.py
from django.shortcuts import render
from .models import Proyectos

# Create your views here.
# recuperar los registros de la tabla Projects que maneja nuestro modelo ORM 
# a través una lista de objetos interna y un método .all() que hace referencia a todos sus objetos:
def portfolio(request):
    projects = Proyectos.objects.all() 
    return render(request, "portfolio/portfolio.html")
```


Tenemos que inyectar estos proyectos en el template, para hacerlo simplemente enviamos a la función render un tercer parámetro con un diccionario y los valores que queremos inyectar.


### Actualizamos `urls.py`

Agregamos las dos vistas que venimos trabajando

```python
##primer_proyecto/urls.py
from app_prueba import views as prueba_views
from portfolio import views as portfolio_views

urlpatterns = [
    #Creamos un patrón url, en la raíz del sitio (cadena vacía) desde el que llamaremos a la vista views.home que tiene el nombre home.
    path('',prueba_views.home, name="home"), 
    path('about/',prueba_views.about, name="about"), 
    path('contact/',prueba_views.contact, name="contact"), 
    path('portfolio/',portfolio_views.portfolio, name="portfolio"), #en este indicamos que utilice la vista porfolio
    path('admin/', admin.site.urls),
]
```

Es una Buena práctica separar las apps, para organizar bien el código y que pueda
escalar. Nos queda en la vista portfolio, hacer referencia al modelo Project para recuperar
sus instancias y enviarlas al template, así que lo importamos arriba del todo:

```python
##portfolio/views.py
from .models import Proyectos
def portfolio(request):
    projects = Proyectos.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects': projects })
```
Se recuperan los registros de la tabla Projects que maneja nuestro modelo ORM a
través de una lista de objetos interna y un método .all() que hace referencia a todos
sus objetos.

Finalmente tenemos que inyectar estos proyectos en el template. Para hacerlo
simplemente enviamos a la función render un tercer parámetro con un diccionario
y los valores que queremos inyectar


### portfolio.html

En portfolio creamo la carpeta templates y luego otra carpeta llamada portfolio

`portfolio/templates/portfolio`

```html
<!-- heredamos del template base-->
{% extends 'app_prueba/base.html' %}
<!-- cargamos los recursos estaticos-->
{% load static %}
<!-- identificamos el contenido dinamico del titulo-->
{% block title %}Portafolio{% endblock %}
<!-- identificamos el contenido dinamico del imagen de fondo-->
{% block background %}{% static 'app_prueba/img/portfolio-bg.jpg' %}{% endblock %}
<!-- identificamos el contenido dinamico del header-->
{% block headers %}
    <h1>Portafolio</h1>
    <span class="subheading">Proyectos</span>
{% endblock %}
<!-- mostramos los proyectos de la base de datos-->
{% block content %}
<!-- usamos el template tag for que nos permite iterar y mostrar atributos-->
    {% for project in projects %} 
        <!-- Proyecto -->
        <div class="row project">   
            <div class="col-lg-3 col-md-4 offset-lg-1">
               {% if project.image %}

                <img class="img-fluid" src="{{project.image.url}}" alt="">
                
                {% endif %}

            </div>
            <div class="col-lg-7 col-md-8">
                <h2 class="section-heading title">{{project.title}}</h2>   
                <p>{{project.description}}</p>
                {% if project.link %}
                    <p><a href="{{project.link}}">Más información</a></p>
                {% endif %}
            </div>
        </div>
    {% endfor %}
{% endblock %}
``` 
# Formularios

Un formulario HTML es una colecion de elementos dentro del tag `<form></form>` conteniendo al menos un elemento del tipo: `type="submit"`

Consideremos un formulario simple con un solo campo de texto "team":

```html
<form action="/team_name_url/" method="POST">
    <label for="team_name">Enter name: </label>
    <input id="team_name" type="text" name="name_field" value="Default name for team.">
    <input type="submit" value="OK">
</form>
```

El atributo `type` del campo `input` define qué tipo de widget se mostrará. El `name` y el `id` se utilizan para identificar el campo en JavaScript/CSS/HTML, mientras que el `value` define el valor inicial cuando se muestra por primera vez el formulario. El `id` vincula el `<input>` con el `<label>`. 

El `<input type="submit">` se mostrará como un botón de forma predeterminada. Esto se puede presionar para cargar los datos en todos los demás elementos de entrada en el formulario al servidor (en este caso, solo el campo `team_name`). El atributo `method` del formulario define el método HTTP utilizado para enviar los datos y `action` el destino de los datos en el servidor :

* `action`  acción: el recurso/URL donde se enviarán los datos para su procesamiento cuando se envíe el formulario. Si no se establece (o se establece en una cadena vacía), el formulario se enviará de nuevo a la URL de la página actual.

* `method` método: el método HTTP utilizado para enviar los datos: 
    - El método POST siempre debe usarse si los datos van a resultar en un cambio en la base de datos del servidor, ya que puede hacerse más resistente a los ataques de solicitud de falsificación entre sitios.

    - El método GET solo debe usarse para formularios que no cambian los datos del usuario (por ejemplo, un formulario de búsqueda). Se recomienda para cuando desee poder marcar o compartir la URL.


# Formularios en DJANGO    

Los pasos del manejo de formularios de Django son:

1. Mostrar el formulario predeterminado la primera vez que es
solicitado por el usuario.
    -  El formulario puede contener campos en blanco (por ejemplo,
    si está creando un registro nuevo), o puede estar rellenado
    previamente con valores iniciales (por ejemplo, si está
    modificando un registro o si tiene valores iniciales
    predeterminados útiles)
    - El formulario se conoce como no vinculado en este punto
    porque no está asociado con ningún dato ingresado por el
    usuario (aunque pueda tener valores iniciales).
    
2. Recibir datos del 'submit' y vincularlo al formulario.
    
    - La vinculación de datos al formulario significa que los datos
    ingresados por el usuario y cualquier error son guardados para estar disponibles
    cuando necesitamos volver a desplegar el formulario.
    
3. Limpiar y validar los datos. 
    
    - La limpieza de los datos realiza una sanitización de la entrada
    (por ejemplo, remover caracteres no válidos que podrían ser
    usados para enviar contenido malicioso al servidor SQLINJECTIONS) y
    convertirlos en objetos consistente de Python.
    
    - La validación verifica que los valores sean apropiados para el
    campo (por ejemplo, que estén en el rango correcto de fechas,
    no sean demasiado cortos ni demasiado largos, etc.)
    
4. Si algún dato es no válido, volver a mostrar el formulario, esta vez con valores validos rellenados por el usuario y los mensajes de error para los campos con problemas.

5. Si todos los datos son válidos, realizar las acciones requeridas (por ejemplo, guardar los datos, enviar un correo electrónico, devolver el resultado de una búsqueda, cargar un archivo, etc)

6. Una vez todas las acciones se hayan completado, redirigir al usuario a otra página.


Vamos a crear una nueva app contacto

```bash
python3 manage.py startapp contact
```

Agregamos la app contact en el archivo `settings.py`

```python
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'prueba',
'portfolio.apps.PortfolioConfig',
'contact',
]
```

Trasladamos la vista contact a la nueva app:

```python
##contact/views.py
from django.shortcuts import render
# Create your views here.
def contact(request):
    return render(request, "contact/contact.html")
```

Agregamos la vista al archivo `urls.py` del proyecto:

```python
from contact import views as contact_views


urlpatterns = [
    path('',views_app_prueba.home, name="home"), 
    path('contact/',contact_views.contact, name="contact"), 
    path('about/',views_app_prueba.about, name="about"), 
    path('portfolio/',portfolio_views.portfolio, name="portfolio"), 
    path('admin/', admin.site.urls),
]

```



Agregamos el template de `contact.html` en `contact/templates/contact`:

```html
{% extends 'app_prueba/base.html' %}

{% load static %}

{% block title %}Contacto{% endblock %}

{% block background %}{% static 'app_prueba/img/contact-bg.jpg' %}{% endblock %}

{% block headers %}
    <h1>Contacto</h1>
    <span class="subheading">Envianos tus dudas</span>
{% endblock %}
```

## Creando el objeto formulario



Hay que crear un archivo `forms.py` dentro de la app contact, heredando de una clase llamada `Form` que hay en el módulo `forms`.

Es parecido a crear un modelo, ya que debemos indicar los campos y su tipo. El nuestro tiene tres: 

- Nombre: que será una cadena de texto. 
- Email: que tiene su propio tipo.
- Contenido:

Es lo mínimo necesario para que alguien pueda enviarnos un mensaje y le podamos responder. Hay campos para todo: cadenas, números, emails, fechas, opciones desplegables, ficheros, etc.

https://docs.djangoproject.com/en/dev/ref/forms/fields/#built-in-fieldclasses

```python
from django import forms
class ContactoForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea())
```

Es en esta instancia donde podemos agregar todo lo que necesitemos en el formulario HTML sin tener que escribir html, por ejemplo podemos probar que pasa si agregamos los campos de fechas y un selector.

```
lista=[('A','30 Cuotas'),  ('B','60 Cuotas'), ('C', '90 Cuotas')]
day = forms.DateField(initial=datetime.date.today)
item_lista= forms.CharField(label='Que opciones elegis?', widget=forms.Select(choices=lista))
```


Los campos vienen definidos en el módulo forms y para el nombre se utiliza el atributo label. Por defecto estos campos se renderizan como tags <input>, pero se pueden cambiar estableciendo un tipo de widget, como en el caso el contenido donde queremos mostrar un tag <textarea>.

    
Lo que tenemos que hacer ahora, igual que en el modelo, crear una instancia de este formulario en la vista y enviarla al template,

```python
from django.shortcuts import render
from .forms import ContactoForm

def contact(request):
    contact_form = ContactoForm
    return render(request, "contact/contact.html", {'form':contact_form})
```
    
Todavia no vemos ningun formulario, para eso tenemos que agregar en el templete el formulario que acabamos de crear.

## Agregamos el form al template de contacto:    
    
En el template de `contact.html` ingresamos el formulario creado, con el 'template tag' form, en este caso lo ponemos dentro de una tabla, podría ser una lista o párrafo.
    
    
```html
{% block content %}
<div class="row"> 
    <div class="col-lg-8 col-md-10 mx-auto">
      <!-- Formulario de contacto-->
        <form action="" method="POST">
        <div class="form-group">
            
          <table>
            {{form.as_p}}
          </table>
            
          <input type="submit" value="Enviar" />
            
        </div>
    
        </form>
    <!--{{request.POST}}-->
    </div>
</div>
{% endblock %}
    
```
Hay dos métodos para enviar un formulario: POST y GET. El método GET es visible a simple vista, se añade a la URL de la petición con un interrogante al final. Si no interesa que las peticiones se vean en la barra de direcciones, se utiliza el método POST que se envía oculto.
    
En cuanto al atributo action sería la página donde enviamos el formulario, al no establecer ningún valor, se interpretará que la petición POST debe realizarse contra la página actual, que en nuestro caso será `/contact/` de la web.

Ahora si podemos ver el formulario! 

## Enviando el formulario

Que pasa si intentamos enviar informacion usando el formulario?

    
## CSRF (Cross-Site Request Forgery)


Django tiene un mecanismo que evita que podamos hacer HTTP requests desde cualquier lugar, lo cual puede ser peligroso, por eso debemos asegurarnos que el request sale desde la pagina `contact.html`. Esto se hace generando un token que se envia con el formulario para verificar que el requests proviene de nuestro sitio.
    
```python
 ...
<form action="" method="POST">
      {% csrf_token %}
      <div class="form-group">
...     
```

Hasta aca pudimos generar un formulario usando django y vemos que envia la informacion ingresada por el usuarix, ahora vamos a mostrar un mensaje al usuario de envio exitoso.  Para esto tenemos que modificar la vista teniendo en cuenta que cuando el formulario se envia con `action = ''` por defecto se vuelve a cargar la pagina.
          
Como ejemplo sencillo agreguemos en la template del contact que muestre un mensaje cuando el formulario haya sido enviado, podriamos incluso usar la informacion del formulario. Cambiemos la vista para que renderee el template `contact.html` a la cual le enviaremos la variable `name` bajo el nombre 'enviado':          

                    
          
```python
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
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            return render(request,'contact/contact.html',{'enviado': name})         
    return render(request,'contact/contact.html',{'form': contact_form})
```
          

Ahora modificamos el `block content` del template `contact.html` usando un bloque if que solo se mostrara cuando la vista sea generada con la variable `enviado`: 
         
```html          

{% block content %}
{% if enviado %}
<div class="col-lg-8 col-md-10 mx-auto">

<p><b>Gracias {{enviado}} !</b></p>
<p><b>Tu mensaje se envio correctamente, en breve nos pondremos en contacto</b></p>

</div>

{% else %}

<div class="row"> 
    <div class="col-lg-8 col-md-10 mx-auto">
    <!-- Formulario de contacto-->
        <form action="" method="POST">
        {% csrf_token %}
        <div class="form-group">
            
        <table>
            {{form.as_p}}
        </table>
            
        <input type="submit" value="Enviar"/>            
        </div>    
        </form>
    <!--{{request.POST}}-->
    </div>
</div>
{% endif %}
{% endblock %}
```          

# Sesiones

Las sesiones son el mecanismo que usa Django (y la mayor parte de Internet) para
guardar registro del "estado" entre el sitio y un navegador en particular. Las
sesiones te permiten almacenar información arbitraria por navegador, y tener esta
información disponible para el sitio cuando el navegador se conecta. Cada pieza
individual de información asociada con una sesión se conoce como "clave", que se
usa tanto para guardar como para recuperar la información.

Django usa una cookie que contiene un id de sesión específica para identificar cada
navegador y su sesión asociada con el sitio. La información real de la sesión se
guarda por defecto en la base de datos del sitio (esto es más seguro que guardar
la información en una cookie, donde es más vulnerable para los usuarios
maliciosos). Puedes configurar Django para guardar la información de sesión en
otros lugares (caché, archivos, cookies "seguras"), pero la opción por defecto es
una buena opción y relativamente segura.

Las sesiones fueron automáticamente habilitadas cuando creamos el sitio web del
proyecto. La configuración está establecida en las secciones INSTALLED_APPS y
MIDDLEWARE del archivo del proyecto `settings.py`:

```python
INSTALLED_APPS = [
...
'django.contrib.sessions',
....
MIDDLEWARE = [
...
'django.contrib.sessions.middleware.SessionMiddleware',
....

``` 

## Usando las sesiones

Se puede usar el atributo session en la vista desde el parámetro `request` (una
HttpRequest que se envía como el primer argumento a la vista). Este atributo de
sesión representa la conexión específica con el usuario actual (o para ser más
preciso, la conexión con el navegador actual, como se identifica mediante la id de
sesión en la cookie del navegador para este sitio).

**El atributo session es un objeto tipo diccionario** que puedes leer y escribir tantas
veces como quieras en tu vista, modificándolo como desees. Puedes realizar todas
las operaciones normales de diccionario, incluyendo eliminar toda la información,
probar si una clave está presente, iterar a través de la información, etc. Sin
embargo, la mayor parte del tiempo solo usarás la API estándar de "diccionario"
para recuperar y establecer valores.

Se puede recuperar, establecer o eliminar información, asociada con la sesión
actual (del navegador). La API ofrece también una cantidad de métodos adicionales que se usan
mayoritariamente para administrar la cookie de sesión asociada. Por ejemplo, hay
métodos para probar si el navegador cliente soporta cookies, establecer y revisar
las fechas de expiración de las cookies, y para eliminar sesiones expiradas del
almacén de datos.

https://docs.djangoproject.com/en/4.0/topics/http/sessions/

### Guardando la información de la sesión

Por defecto, Django solo guarda información en la base de datos de sesión y envía
la cookie de sesión al cliente cuando la sesión ha sido modificada (asignada) o
eliminada.


Vamos a agregar un conteo de visitas al home, en el archivo `app_prueba/views.py` vamos a agregar en la función que renderiza la
`home` el contador. Para eso obtenemos el valor de la clave de sesión `num_visits`, estableciendo el valor a 0 si no había sido establecido previamente. Cada vez que se recibe la solicitud, incrementamos el valor y lo guardamos de vuelta en la sesión (para la siguiente vez que el usuario visita la página).

Necesitamos usar la variable `context` y agregar la variable `num_visits`para envíar al template `home.html`.

```python
##app_prueba/views.py
def home(request):
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    context = {'num_visits':num_visits}
    return render(request,"app_prueba/home.html", context=context)
```


Por ultimo vamos a modificar el template del home, al final de la sección "content": Notemos que llamamos las llaves del diccionario `context` con doble llave: `{{key1}}`:

```html
<!-- app_prueba/templates/app_prueba/home.html  -->
<!-- agregamos dentro de la pagina el contador de visitas-->
{% block content %}
<p>Ha visitado esta pagina {{ num_visits }}{% if num_visits == 1 %} vez {% else %}
veces {% endif %}.</p>
{% endblock %}
```


# Autentificaciones

Django proporciona un sistema de autenticación y autorización ("permisos"), construido sobre el framework de sesión, que permite verificar credenciales de usuario y definir qué acciones puede realizar cada usuario. El framework incluye modelos para Users y Groups (una forma genérica de aplicar permisos a más de
un usuario a la vez), permisos/indicadores (permissions/flags) que designan si un usuario puede realizar una tarea, formularios y vistas para iniciar sesión en los usuarios y view tools para restringir el contenido.

Tambien nos permite habilitar la autenticación de usuarios en el sitio web, crear nuestras propias páginas de login y logout, añadir permisos a los modelos, y controlar el acceso a las páginas. El sistema de autenticación es muy flexible, y puedes crear URLs, formularios, vistas y plantillas simplemente llamando a la API provista para loguear al usuario.


La autenticación fue habilitada automáticamente cuando creamos el sitio web (lo podemos revisar en el archivo `settings.py`).

```
##settings.py
INSTALLED_APPS = [
...
'django.contrib.auth', #Core authentication framework and its default models.
'django.contrib.contenttypes', #Django content type system (allows permissions
to be associated with models).
....
MIDDLEWARE = [
...
'django.contrib.sessions.middleware.SessionMiddleware', #Manages sessions
across requests
...
'django.contrib.auth.middleware.AuthenticationMiddleware', #Associates users
with requests using sessions
```

## Creando usuarios y grupos

Creamos nuestro primer usuario cuando revisamos el sitio de administración de Django, creado con el comando:

`python3 manage.py createsuperuser`

Nuestro superusuario ya está autenticado y tiene todos los permisos, así que necesitaremos crear un usuario de prueba que represente un usuario normal del sitio.

Vamos a usar el sitio de administración para crear los grupos y logins de nuestro sitio web, ya que es una de las formas más rápidas de hacerlo.

Ingresamos al sitio usando las credenciales de la cuenta de tu superusuario. El nivel superior del sitio de administración "Admin site" muestra todos tus modelos, ordenados por la aplicación por defecto de Django "django application". 

Desde la sección de Autenticación y Autorización puedes dar clic en los enlaces de Usuarios "Users" y Grupos "Groups" para ver todos sus registros existentes.
 
El sitio de administrador creara el nuevo usuario e inmediatamente ira a la pantalla de Change user "Cambios del usuario" donde puedes cambiar nombre de usuario "Username" y agregar información para los campos opcionales del modelo de Usuario "User". Estos campos incluyen el primer nombre "first name", el apellido "last name", la dirección de correo electrónico "email adress", los estados de los usuarios y sus permisos "users status and permissions" (solo el indicador Active "Activo" debería ser activado). Mas se puede especificar los grupos y permisos del usuario, y ver datos importantes relacionados a el usuario (ej.: la fecha en que se agregó y la fecha del último inicio de sesión)

## Configurando las vistas de autenticación

Django provee todo lo necesario para crear las páginas de autenticación para manejar inicio y cierre de sesión y gestión de contraseñas "out of the box". Esto incluye un mapeador de URL, vistas "views" y formularios "forms", pero no incluye las plantillas "templates” (pilas no incluidas).

### URL's del proyecto

Añade el siguiente código al final del archivo `urls.py`:

```python
##urls.py
# importamos la funcion include
from django.urls import include

#Agregamos las direcciones de autenticacion (login, logout, gestion password)
path('accounts/',include('django.contrib.auth.urls'))
```

Básicamente tenemos el login, el logout y varias vistas para manejar la gestión de contraseñas. Recordemos que anteriormente dijimos que lo único que no provee DJANGO son los templates de autenticación, por lo que vamos a hacerlos.



## Templates de la registracion

Todos estos templates tienen que estar en la carpeta `templates\registration`.

- login
- logout
- password_reset_complete
- password_reset_confirm
- password_reset_done
- password_reset_email
- password_reset_form

Luego de haber creado la carpeta templates tenemos que agregarla en `settings.py`:

```python
# importamos el modulo os
import os 

    # …
    TEMPLATES = [
      {
       # …
       'DIRS': [os.path.join(BASE_DIR, 'templates')]
       # …
       
       ]}
```


### Template del login


```html
{% extends 'app_prueba/base.html' %}
{% load static %}
{% block title %}Iniciar sesión{% endblock %}
{% block content %}
<style>.errorlist{color:red;}</style>
<main role="main">
<div class="container">
<div class="row mt-3">
<div class="col-md-9 mx-auto mb-5">
<form action="" method="post">{% csrf_token %}
<h3 class="mb-4">Iniciar sesión</h3>
{% if form.non_field_errors %}
<p style="color:red">Usuario o contraseña incorrectos, prueba de nuevo.</p>
{% endif %}
<p>
<input type="text" name="username" autofocus maxlength="254" required
id="id_username" class="form-control" placeholder="Nombre de usuario"/>
</p>
<p>
<input type="password" name="password" required
id="id_password" class="form-control" placeholder="Contraseña"/>
</p>
<p><input type="submit" class="btn btn-primary btn-block"
value="Acceder"></p>
</form>
</div>
</div>
</div>
</main>
{% endblock %}
```

Ahora para visualizar el login entremos a http://127.0.0.1:8000/accounts/login/

Si intentas iniciar sesión tendrá éxito y serás redirigido a otra página (por defecto será http://127.0.0.1:8000/accounts/profile/). El problema aquí es que, por defecto, Django espera que después de iniciar sesión seas llevado a una página de perfil (que podrá ser el caso o no). Como no has definido esta página todavía obtendremos un error

Abre la configuración del `settings.py` y añade al final el texto de abajo. Ahora cuando inicies sesión deberías ser redirigido a la página de inicio por defecto.

```python
##settings.py
# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
```

### Template del logout

Si navegás a la url de cierre de sesión (http://127.0.0.1:8000/accounts/logout/) verás un extraño comportamiento — tu usuario cerrará la sesión, pero serás llevado a la página de cierre de sesión del Administrador. Eso no es lo que quieres, ademas se el enlace de inicio de esa página te lleva a la pantalla del inicio de sesión del Administrador.

Vamos a crear el template de logout

```html
{% extends 'app_prueba/base.html' %}
{% block content %}
<p>Has salido de la sesión!</p>
<a href="{% url 'login'%}">Hace clic aca nuevamente para iniciar sesión.</a>
{% endblock %}
```

Esta plantilla es muy simple. Tan sólo muestra un mensaje informándote que has cerrado sesión y provee un enlace que puedes pulsar para volver a la página de inicio de sesión. Ahora queremos que cuando el usuario salga, vuelva al home, no nos tenemos que olvidar de redirecciones al home:

```python
##settings.py
# Redirect to home URL after logout (Default redirects to /accounts/profile/)
LOGOUT_REDIRECT_URL = '/'
```

## Insertando el login/logout en el header

En este punto sería interesante modificar el diseño del menú superior para mostrar estas opciones en lugar de las del administrador. 

Vamos a modificiar la template `base.html` insertando estos 'li' en la 'ul' de la navbar:

```html
{% if not request.user.is_authenticated %}
<li class="nav-item">
<a class="nav-link" href="{% url 'login' %}">Acceder</a>
</li>
{% else %}
<li class="nav-item">
<a class="nav-link" href="{% url 'logout' %}">Salir</a>
</li>
{% endif %}
```
          
Ahora si ya tenemos listo el login/logout.

## Permisos de usuario

Puedes obtener información en las plantillas sobre el usuario que actualmente ha iniciado sesión con la variable de plantillas `{{ user }}` (esto se añade por defecto al contexto de la plantilla cuando configuras el proyecto)

Es típico que primero pruebes con la variable de plantilla `{{ user.is_authenticated}}` para determinar si el usuario puede ver el contenido específico, como hicimos cuando agregamos en el menú, lo botones de acceso y salir.

Ahora podemos restringir si el usuario puede ver las vistas o no. La forma más fácil para restringir el acceso a tus funciones es aplicar `login_required` a tu función de vista. Si el usuario ha iniciado sesión entonces tu código de vista se ejecutará como normalmente lo hace. Si el usuario no ha iniciado sesión, se redirigirá a la URL de inicio de sesión definida en tu configuración de proyecto (settings.LOGIN_URL), pasando el directorio absoluto actual como el parámetro URL next.

Si el usuario tiene éxito en el inicio de sesión entonces será devuelto a esta página, pero esta vez autenticado. Por ejemplo, vamos a restringir que para ver los proyectos hay que estar autenticado agregandole el decorador `@login_required` la vista: 

```python
##portfolio/views.py
#importamos el decorador
from django.contrib.auth.decorators import login_required

#usamos el decorador
@login_required
def portfolio(request):
 html_response = "<h1>Proyectos/h1>"
 return HttpResponse(html_response)
```

Muchas veces hay que limpiar el cache del navegador para comprobar que funciona correctamente.


## Formulario de reinicio de contraseña

Este es el formulario para obtener la dirección del correo electrónico del usuario (para enviar el correo de reinicio de contraseña).

Vamos a crear el template `password_reset_form.html`

```html
{% extends 'app_prueba/base.html' %}
{% block content %}
<form action="" method="post">{% csrf_token %}
{% if form.email.errors %} {{ form.email.errors }} {% endif %}
<p>{{ form.email }}</p>
<input type="submit" class="btn btn-default btn-lg" value="Reiniciar contraseña" />
</form>
{% endblock %}
```

### Correo electrónico de reinicio de contraseña

Esta plantilla suministra el texto HTML del correo electrónico, y contiene el enlace de reseteo que enviaremos a los usuarios.
Crea `password_reset_email.html` y establece el siguiente contenido:

```html
Hemos recibido una solicitud de reinicio de contraseña para el correo {{ email }}. 
Sigue el siguiente link: {{ protocol}}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}
```

## Reinicio de contraseña hecho

Este formulario es mostrado después de que tu dirección de correo electrónico
haya sido recogida. Vamos a crear `password_reset_done.html` y establecer el siguiente contenido:

```html
{% extends 'app_prueba/base.html' %}
{% block content %}
<p>Hemos enviado un correo electrónico con las instrucciones para configurar una
nueva contraseña
. Si no arriba en algunos minutos, por favor revisa la carpeta SPAM</p>
{% endblock %}
``` 

## Confirmación de reinicio de contraseña

Esta página es donde introduces una nueva contraseña después de clickear el enlace en el correo electrónico de reinicio de contraseña. 
Creamos `password_reset_confirm.html` con el siguiente contenido:

```html
{% extends 'app_prueba/base.html' %}
{% load static %}
{% block content %}
{% if validlink %}
<p>Por favor ingrese su nueva contraseña.</p>
<form action="" method="post">
<div style="display:none">
<input type="hidden" value="{{ csrf_token }}" name="csrfmiddlewaretoken">
</div>
<table>
<tr>
<td>{{ form.new_password1.errors }}
<label for="id_new_password1">Nueva contraseña:</label></td>
<td>{{ form.new_password1 }}</td>
</tr>
<tr>
<td>{{ form.new_password2.errors }}
<label for="id_new_password2">Confirme Contraseña:</label></td>
<td>{{ form.new_password2 }}</td>
</tr>
<tr>
<td></td>
<td><input type="submit" value="Cambiar mi contraseña" /></td>
</tr>
</table>
</form>
{% else %}
<h1>Fallo el reinicio de contraseña</h1>
<p>El link de reinicio de contraseña es invalido, posiblemente porque ya fue usado.
Por favor solicite un nuevo reinicio de contraseña.</p>
{% endif %}
{% endblock %}
```

## Reinicio de contraseña completado

Este es el último paso de la plantilla de reinicio de contraseña, que es mostrada para notificarte cuando el reinicio de contraseña ha tenido éxito. 

Creamos `password_reset_complete.html`, y establece el siguiente contenido:

```html
{% extends 'app_prueba/base.html' %}
{% block content %}
<h1>La contraseña ha sido cambiada con éxito!</h1>
<p><a href="{% url 'login' %}">Desea iniciar sesión nuevamente?</a></p>
{% endblock %}
```

Por ultimo agregamos en el template `login.html` la opción de olvido de contraseña debajo del formulario

```html
<!--Opción de olvido de contraseña-->
<p><a href="{% url 'password_reset' %}">Olvido su contraseña?</a></p>
```

Para poder probar el reinicio de correo sin enviar un email, podemos hacer lo siguiente:

Establece la siguiente línea al final del archivo settings.py. Esto registra en la consola cualquier envío de correo electrónico (y así puedes copiar el enlace de reinicio de contraseña desde dicha consola).

```python
##settings.py
#Test email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
Solo funciona si se introducen mails de usuarios que ya existan en la db.

## Registracion

Vamos a generar un formulario de registro, sus vistas, templates y modelos.

Primero agregamos el form de registro:

```python
##app_prueba/forms.py
from django import forms

class RegistroForm(forms.Form):
    cliente_id = forms.CharField(label="cliente_id", required=True)
    email = forms.CharField(label="email", required=False)
    pwd = forms.CharField(label="pwd", required=False)
```

Ahora creamos la vista y agregamos el form:

```python
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
        print(cliente_id,email,pwd)
        user = User.objects.create_user(cliente_id, email, pwd)
        user.save()
        print('creado')
        #En lugar de renderizar el template de prestamoo hacemos un redireccionamiento enviando una variable OK
        return redirect(reverse('login'))
    return render(request,"app_prueba/registro.html",{'form': registro_form})
 ```
Y por ultimo creamos la template `registro.html`:

```html
{% extends 'app_prueba/base.html' %}
{% load static %}
{% block title %}Registro de Usuarios{% endblock %}
{% block content %}
<style>.errorlist{color:red;}</style>
<main role="main">
<div class="container">
<div class="row mt-3">
<div class="col-md-9 mx-auto mb-5">
<form action="" method="post">{% csrf_token %}
<h3 class="mb-4">Registro</h3>

<p>
<input type="text" name="cliente_id" autofocus maxlength="254" required
id="id_username" class="form-control" placeholder="DNI de usuario"/>
</p>
<p>
    <input type="text" name="email" autofocus maxlength="254" required
    id="id_username" class="form-control" placeholder="Mail"/>
    </p>
<p>
<input type="password" name="pwd" required
id="id_password" class="form-control" placeholder="Contraseña"/>
</p>
<p><input type="submit" class="btn btn-primary btn-block"
value="Acceder"></p>
<!--Opción de olvido de contraseña-->

</form>
</div>
</div>
</div>
</main>
{% endblock %}
```
Agregamos el link al registro en el `login.html` abajo del 'olvido su contrasemna':

```html
<p><a href="{% url 'registro' %}">Registrese</a></p>
```
Finalmente debemos especificar en `urls.py` la vista de registro:

```python

urlpatterns = [
    path('',views_app_prueba.home, name="home"), 
    path('contact/',contact_views.contact, name="contact"), 
    path('about/',views_app_prueba.about, name="about"), 
    path('portfolio/',portfolio_views.portfolio, name="portfolio"), 
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/registro',views_app_prueba.registro, name="registro"), 
]
```

          
Agreguemos al `home.html` un mensaje de bienvenida para el usuario

```html
          Bienvenido {{name}} !
```

Para que esto funcione debemos modificar la vista home enviando la variable `request.user.username`:
          
```python          
    def home(request):
    if request.user.username:
        return render(request,"app_prueba/home.html", {'name' : request.user.username})
    else:    
        return render(request,"app_prueba/home.html")
```        
# Importando db

Vamos a descagar la siguiente [db](https://colab.research.google.com/drive/1DfkpjRz5Q5mHvBZ75n0W6p5ofptBeRCx?usp=sharing) y la dejamos en la carpeta del proyecto, luego la agramos en `settings.py`:

```
    'old': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'old.db',
    }
```

Para importar los modelor al proyecto necesitamos usar el comando:

```
python3 manage.py inspectdb --database old > old_db.py
```
En ese archivo `old_db.py` estan los modelos que necesitamos copiar en `models.py` (Tener cuidado con la columna 'id' y seguir las instrucciones).

Django ahora administra ambas db!

Ahora si vamos a cambiar la vista del about para mostrar todos los participantes!.

```python
from .models import Participantes
def about(request):
    nosotros = Participantes.objects.using('old').all() 
    return render(request, "app_prueba/about.html", {'participantes': nosotros })
```
# Queries


## Create

Vamos a generar el modelo de los formularios de contacto en la db para guardalos, ademas vamos agregarle al formulario de contacto sobre cual proyecto quiere el usuario contactarse.

Primero agregamos esto al form de contacto:

```contact\forms.py
lista=[('3','Api'),  ('4','HomeBanking'), ('5', 'Movil')]
date = forms.DateField(initial=datetime.date.today)
proyecto_id= forms.CharField(label='Que proyecto te intereso?', widget=forms.Select(choices=lista))
```

Para representar los datos de la tabla de la base de datos con objetos de Python, Django utiliza un sistema intuitivo: una clase modelo representa una tabla de la base de datos y una instancia de esa clase representa un registro particular en la tabla de la base de datos.
Para crear un objeto, ejecútelo usando argumentos de palabras clave para la clase modelo, luego llame a `save()` para guardarlo en la base de datos. 

Primero vamos a crear la clase contacto, para guardar todos los envíos de contacto que nos hagan los usuarios, para eso vamos a ir al modelo de nuestra app contact, vamos a guardar el nombre, el correo, el mensaje, la fecha de envio, de modificación y el proyecto.


```python
from portfolio.models import Proyectos

class Contact(models.Model):
  name= models.CharField(max_length=100)
  email= models.EmailField()
  content= models.TextField()
  date= models.DateField()
  project = models.CharField(max_length=100)
  def __str__(self): 
    return self.name
```

Una vez creada la clase vamos a realizar las migraciones correspondientes con los comandos

```bash
python3 manage.py makemigrations 
python3 manage.py migrate
```

Si abrimos el archivo `db.sqlite3` del sitio de prueba, vamos a poder ver que se creó la tabla contacto, con los campos que definimos.
Ahora vamos a la vista que teníamos para procesar el formulario de contacto. Los campos que recibimos los vamos a guardar en la base, adicionalmente vamos a referenciar a un proyecto, para tal fin vamos a obtener el proyecto de id 1, pero se podría modificar el formulario para preguntarlo.

Ahora vamos a modificar la vista que teníamos para procesar el formulario de contacto. Los campos que recibimos los vamos a guardar en la base.

```python
##contact/views.py
#importamos el modelo y el formulario
from .forms import ContactoForm
from .models import Contact

#agregamos esto enla vista
if contact_form.is_valid():
    nameReceived = request.POST.get('name','')
    emailReceived = request.POST.get('email','')
    contentReceived = request.POST.get('content','')
    date = request.POST.get('date','')
    proyecto_id= request.POST.get('proyecto_id','')
    contacto = Contact(name=nameReceived,email=emailReceived,content=contentReceived,date=date, project=str(proyecto_id))
    contacto.save()
    return render(request,'contact/contact.html',{'enviado': nameReceived})   
```

## Read

En términos de SQL, un QuerySet equivale a una declaración SELECT y un filtro es una cláusula limitante como WHERE o LIMIT.
Podemos obtener un QuerySet usando el Manger de nuestro modelo. Cada modelo tiene al menos un Manager y llama objetos de forma predeterminada.
Solo se puede acceder a los Managers a través de clases de modelo, en lugar de instancias de modelo, para imponer una separación entre las operaciones de "nivel de tabla" y las operaciones de "nivel de registro". 

Ejemplo:
```python
>>> Contact.objects
<django.db.models.manager.Manager object at ...>
>>> b = Contact(name=’victor’,email=’victor@gmail.com’,content=content,pub_date =date.today())
>>> b.objects
Traceback:
...
AttributeError: "Manager isn't accessible via Contact instances."
```

El Manager es la fuente principal de QuerySets para un modelo. Por ejemplo, `Contact.objects.all()` devuelve un QuerySet que contiene todos los objetos (filas) Contact en la base de datos.

Vamos a importar desde una db previamente creado todos los participantes de los proyectos y generar una vista para la url `\about` que permita al usuario visualizar y filtrar participantes de los diferentes proyectos.

Primeramente generamos el template, la vista y agregamos la url de la pagina `\about` no vamos a generar otra app, lo hacemos sobre `app_prueba` para simplicar un poco.


```html
<!-- heredamos del template base-->
{% extends 'app_prueba/base.html' %}
<!-- cargamos los recursos estaticos-->
{% load static %}
<!-- identificamos el contenido dinamico del titulo-->
{% block title %}Nosotros{% endblock %}
<!-- identificamos el contenido dinamico del imagen de fondo-->
{% block background %}{% static 'app_prueba/img/portfolio-bg.jpg' %}{% endblock %}
<!-- identificamos el contenido dinamico del header-->
{% block headers %}
    <h1>Quienes somos:</h1>

{% endblock %}
<!-- mostramos los proyectos de la base de datos-->
{% block content %}
<!-- usamos el template tag for que nos permite iterar y mostrar atributos-->
    {% for persona in participantes %} 
        <!-- Proyecto -->
        <div class="row project">   
            <div class="col-lg-1 col-md-1 offset-lg-4 offset-md-4">
                {% if persona.img %}
                <img class="img-fluid" src="{{persona.img}}" alt="">
                {% endif %}
            </div>

            <div class="col-lg-5 col-md-3 offset-lg-3 offset-md-4">
                <h2 class="section-heading title">{{persona.name}} {{persona.last_name}}</h2>      
                <p>Equipo: {{persona.team}}</p>
                <p>Proyecto: {{persona.proyect_id}}</p>

            </div>
        </div>
    {% endfor %}
{% endblock %}
```
Podemos ver que la plantilla ya esta lista para recibir la variable participantes, debemos en la vista escribir el codigo para importar la tabla participantes y filtrar por proyecto e incluso ordenar por nombre.



## Vamos agregar un form que sirva como filtro y nos permita hacerle consultas a la db.

```python

lista=[('3','Api'),  ('4','HomeBanking'), ('5', 'Movil')]
lista2=[(1,'Back'),  (2,'Front'), (3, 'UX')]

class FiltroParticipantes(forms.Form):
    name = forms.CharField(label="Contiene:", required=False)
    #aca agregamos en el form, el campo de la fecha pero lo ocultamos en el template
    proyecto_id= forms.CharField(label='Que proyecto te intereso?', widget=forms.Select(choices=lista))
    team= forms.CharField(label='Que equipo te intereso?', widget=forms.Select(choices=lista2))
``` 
Actualizamos la vista:

```python
from .forms import FiltroParticipantes
from .models import Participantes
def about(request):
    nosotros = Participantes.objects.using('old').all() 
    filtro_form = FiltroParticipantes
    return render(request, "app_prueba/about.html", {'participantes': nosotros , 'form': filtro_form})
```
Y luego el template del `about.hml`:

```html
<div class="row project">   

    <div class="col-lg-5 col-md-3 offset-lg-3 offset-md-4">
        <form action="" method="POST">
            {% csrf_token %}
            <div class="form-group">
                
            <table>
                {{form.as_p}}
            </table>
                
            <input type="submit" value="Filtrar"/>            
            </div>    
            </form>
    </div>
</div>
```
## Filtros: 

`Contact.objects.filter(pub_date__year=2020)`

En nuestro caso como tenemos dos db, tenemos que especificar:

`Participantes.objects.using('old').filter(proyecto_id=2)` 

Tenemos que volver a modificar la vista del about, usando un if para responder al formulado enviado:

```python
from .forms import FiltroParticipantes
from .models import Participantes
def about(request):
    nosotros = Participantes.objects.using('old').all() 
    filtro_form = FiltroParticipantes
    if request.method == "POST":
        filtro_form = filtro_form(data=request.POST)
        proyecto_id = request.POST.get('proyecto_id','')
        nosotros = Participantes.objects.using('old').filter(proyect_id=proyecto_id) 
        return render(request, "app_prueba/about.html", {'participantes': nosotros , 'form': filtro_form})
    return render(request, "app_prueba/about.html", {'participantes': nosotros , 'form': filtro_form})
```

### Varios filtros

El resultado de refinar un QuerySet es en sí mismo un QuerySet, por lo que es posible encadenar refinamientos. Por ejemplo:

`filter_contacts = Contact.objects.filter(name='Santiago').exclude(pub_date__gte=datetime.date.today()).filter(pub_date__year=2020)`

Esto toma el QuerySet inicial de todas las entradas en la base de datos, agrega un filtro, luego una exclusión y luego otro filtro. El resultado final es un QuerySet que contiene todas loss contactos con nombre Santiago, que se publicaron entre el 2020 y el día actual

### Ordenando QuerySets

Podemos ordenar los resultados que nos trae un QuerySet con el método order_by, pasando como parámetro el campo por el cual ordenamos. Por default, es ascendente.

`filter_contacts = Contact.objects.all().order_by('name')`

### Campos de búsqueda

Las búsquedas de campo son la forma de especificar una cláusula SQL WHERE. Se especifican como argumentos de palabras clave para los métodos de QuerySet filter(), exclude() y get().

Los argumentos de palabras clave de búsquedas básicas toman la forma:

`field__lookuptype : value (Con doble guión bajo)`

Ejemplos de lookuptype:

- exact: Devuelve una coincidencia complete con el parámetro de busqueda: `filter_contacts = Contact.objects.filter(name__exact='Santiago')`
- iexact: Deveulve una coincidencia sin importar mayúsculas o minuscuals `filter_contacts = Contact.objects.filter(name__iexact='santiago')`
- contains: Se comporta como el LIKE de SQL `filter_contacts = Contact.objects.filter(name__contains='tiago')`
- lte: Se comporta como menor igual <= `filter_contacts = Contact.objects.filter(pub_date__lte=date.today())`
- gte: Se comporta como mayor igual >= `filter_contacts = Contact.objects.filter(pub_date__gte=date.today())`


## Update

Actualizando multiples objetos

A veces deseamos establecer un campo en un valor particular para todos los objetos en un QuerySet. Para esto usamo el método update().

Por ejemplo actualicemos la fecha de modificación de todos los contactos del año 2020:

`Contact.objects.filter(pub_date__year=2020).update(mod_date=date.today())`


## Delete

El método de eliminación es delete(). Este método elimina inmediatamente el objeto y devuelve la cantidad de objetos eliminados y un diccionario con la cantidad de eliminaciones por tipo de objeto.

`Contact.objects.filter(name='Silvina').delete()`


# Seguridad
