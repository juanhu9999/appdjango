from django.shortcuts import render
from django.http import HttpResponse
from app_uno.models import Curso
from app_uno.forms import curso_formulario

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

def form_api(request):
    if request.method == "POST":
        mi_formulario = curso_formulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "app_uno/inicio.html")
        else:
            mi_formulario = curso_formulario()
        
        return render(request, "app_uno/form_api.html")

