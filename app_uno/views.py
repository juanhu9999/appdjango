from django.shortcuts import render
from django.http import HttpResponse
from app_uno.models import Curso

# Create your views here.
def inicio(request):
    return render(request,"app_uno/inicio.html")

def cursos(request):
    return render(request,"app_uno/cursos.html")

def estudiantes(request):
    return HttpResponse("Vista de los estudiantes")

def curso_formulario(request):

    if request.method == 'POST':

        curso = Curso(nombre=request.POST ['curso'], comision=request.POST ['comision'])

        curso.save()

        return render(request, "app_uno/inicio.html")
    return render(request, "app_uno/curso_formulario.html")



