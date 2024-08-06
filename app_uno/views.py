from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,"app_uno/inicio.html")

def cursos(request):
    return render(request,"app_uno/cursos.html")

def estudiantes(request):
    return HttpResponse("Vista de los estudiantes")

