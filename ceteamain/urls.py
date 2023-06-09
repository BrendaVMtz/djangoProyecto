"""
URL configuration for ceteamain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from inicio import views
from django.contrib import admin
from django.urls import path, include
from sgu import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('home', views.home, name='home'),
    path('registro/', views.registrar, name='registro'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('agregar_tarea/', views.agregar_tarea, name='agregar_tarea'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('sel_perfil/', views.sel_perfil, name='sel_perfil'),
    path('registro_profesor/', views.registro_profesor, name='registro_profesor'),
    path('registro_alumno/', views.registro_alumno, name='registro_alumno'),
    # path('registro_padre/', views.registro_padre, name='registro_padre'),
    # path('registro_salud/', views.registro_salud, name='registro_salud'),
    # # path('verification/', include('verify_email.urls')),
    #path('registro_profesor/',views.registro_profesor),
    #path('registro_salud/',views.registro_profesor),
    # path('comenzar/', include('sgu.urls')),
    # path('aprender/', include('sgl.urls'))
]
