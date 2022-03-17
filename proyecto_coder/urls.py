"""proyecto_coder URL Configuration

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
from unittest.mock import patch
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from proyecto_coder.views import vista_juego
from proyecto_coder.views import edad_usuario
from proyecto_coder.views import nombre_usuario
from proyecto_coder.views import primer_vista,segunda_vista,dia_hora,pag_inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path("primer/",primer_vista),
    path("segunda/",segunda_vista),
    path("diahora/",dia_hora),
    path('nombre-usuario/<nombre>',nombre_usuario),
    path('calc_edad/<edad>',edad_usuario),
    path('inicio/',pag_inicio),
    path("vistajuego/",vista_juego),
    path('admin/',admin.site.urls),
    path('AppCoder/',include('appcoder.urls')),
]
