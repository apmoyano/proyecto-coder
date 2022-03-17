from contextvars import Context
import http
from django.http import HttpResponse
from datetime import datetime
from django.template import Template,Context,loader

def primer_vista(request):
    return HttpResponse("Hola mundo desde mi primer vista en Django")

def segunda_vista(request):
    return HttpResponse("<h1>Titulo 1 </h1> <p>Esto es un parrafo</p>")

def dia_hora(request):
    fecha_hora = datetime.now()
    return HttpResponse(f"<p>Tiempo actual {fecha_hora} </p>")

def nombre_usuario(request,nombre):
    return HttpResponse(f"Tu nombre es {nombre}")

def edad_usuario(request,edad):
    anio_nacimiento = 2022 - int(edad)
    return HttpResponse(f"Tu año de nacimiento es {anio_nacimiento}")

# def pag_inicio(request):
#     archivo = open(r"C:\Users\agus_\Documents\AGUSTIN\PYTHON\django-intro\proyecto_coder\proyecto_coder\templates\page.html")
    
#     nombre = "Agustin"
#     apellido ="Moyano"
#     fecha_hora =datetime.now()

#     listado_calificaciones = [10,9,6]

# #Diccionario con los datos que enviaremos como contexto
#     dict_context ={"nombre":nombre,"apellido":apellido,"fecha_hora":fecha_hora,"listado":listado_calificaciones}


#     plantilla = Template(archivo.read())
    
#     archivo.close

#     context = Context(dict_context)

#     documento = plantilla.render(context)

#     return HttpResponse(documento)

def pag_inicio(request):
    nombre = "Agustin"
    apellido ="Moyano"
    fecha_hora =datetime.now()
    listado_calificaciones = [10,9,6]
    dict_context ={"nombre":nombre,"apellido":apellido,"fecha_hora":fecha_hora,"listado":listado_calificaciones}
    
    plantilla = loader.get_template("page.html")
    
    documento = plantilla.render(dict_context)
    
    return HttpResponse(documento)

def vista_juego(request):
    nombre = "Agustin"
    apellido ="Moyano"
    dict_context ={"nombre":nombre,"apellido":apellido}

    plantilla = loader.get_template("plantilla1.html")
    documento = plantilla.render(dict_context)
    return HttpResponse(documento)