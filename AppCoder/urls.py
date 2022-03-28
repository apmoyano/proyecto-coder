from os import name
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio,name="inicio"),
    path('estudiantes/', estudiantes,name="estudiantes"),
    path('profesores/', profesores,name="profesores"),
    path('cursos/', cursos,name="cursos"),
    path('entregables/', entregables,name="entregables"),
    path('cursoformulario/',formulario_curso, name='formulario'),
    path('buscarcurso/',buscarCurso, name='formulario'),
]
