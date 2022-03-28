from datetime import datetime
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import CursoFormulario
from AppCoder.models import Curso, Estudiante,Profesor,Entregable
# Create your views here.
def inicio(request):
    date_init= datetime.now()
    dict_ctx = {'title': 'Inicio', 'message': 'Bienveni@s'}
    dict_user={"user":"apmoyano","date_init":(date_init)}
    return render(request,"AppCoder/index.html",dict_ctx)

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")

def profesores(request):
    return render(request,"AppCoder/profesores.html")

def cursos(request):
    return render(request,"AppCoder/cursos.html")

def entregables(request):
    return render(request,"AppCoder/entregables.html")

def formulario_curso(request):
    
    if request.method == "POST":

        curso = CursoFormulario(request,"POST")
        print(curso)

        if curso.is_valid:
            data = curso.cleaned_data
            
            curso_nuevo = Curso(data['nombre'],data['camada'])
            curso_nuevo.save()

            return render(request,'AppCoder/index.html')
        
        else:

            curso_form = CursoFormulario()
            
            
        return render(request,'AppCoder/cursosFormularios.html')



def buscarCurso(request):
        pass
