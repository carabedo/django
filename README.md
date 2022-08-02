# DJANGO

- [clase 2](https://github.com/carabedo/django/blob/main/README.md#static-files-models-admin)

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
        <a class="navbar-brand" href="{% url 'home' %}">ITBANK Portafolio de proyectos</a>
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
    <div class="container"><div class="row"><div class="col-lg-8 col-md-10 mx-auto"><ul class="list-inline text-center"><li class="list-inline-item"><a href="#"><span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-envelope fa-stack-1x fa-inverse"></i></span></a></li><li class="list-inline-item"><a href="#"><span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-github fa-stack-1x fa-inverse"></i></span></a></li><li class="list-inline-item"><a href="#"><span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-youtube fa-stack-1x fa-inverse"></i></span></a></li></ul><p class="copyright text-muted">Copyright &copy; 2022 · ITBANK </p></div></div></div></footer>
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
{% block title %}ITBANK Gestion de Proyectos - Inicio {% endblock %}
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

## Models

Nuestro `primer_proyecto` es un ejemplo de un sitio de gestión de proyectos, por eso vamos a necesitar los campos: títulos, descripción, imagen y enlace.

Para tal fin, vamos a crear una nueva app, denominada portfolio:

```bash
python manage.py startapp portfolio
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
    image = models.ImageField(upload_to='projects',verbose_name="Imagen",null=True, blank=True)
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
python manage.py makemigrations portfolio
python manage.py migrate portfolio 
```
Cada vez que hagamos un cambio en nuestro archivo models.py tenemos que ejecutar estos dos comandos para crear una migración y posteriormente aplicarla.

## Admin

Creemos el usuario admin:

```
python manage.py createsuperuser
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


Importamos el modelo `Proyectos` a la vista:


```python
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
from prueba import views as prueba_views
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

```python
<!-- heredamos del template base-->
{% extends 'app_prueba/base.html' %}
<!-- cargamos los recursos estaticos-->
{% load static %}
<!-- identificamos el contenido dinamico del titulo-->
{% block title %}Portafolio{% endblock %}
<!-- identificamos el contenido dinamico del imagen de fondo-->
{% block background %}{% static 'prueba/img/portfolio-bg.jpg' %}{% endblock %}
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
