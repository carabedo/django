# DJANGO

## Instalacion:

UNIX:

```bash
pip3 install django
``` 

WINDOWS:

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



## Creamos nuestro `primer_proyecto`!

```bash
django-admin startproject primer_proyecto
```

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
        html_response += "<p>Línea " + str(i) + "</p>
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
<h1>Bienvenidos a la home</h1>
<h2>Usted esta ubicado en la home</h2>
<p>ITBA 2022</p>
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
