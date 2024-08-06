from django.urls import path
from app_uno.views import inicio, cursos, estudiantes, curso_formulario

urlpatterns = [
    path('', inicio, name="inicio"),
    path('cursos', cursos,name="cursos"),
    path('estudiantes', estudiantes, name="estudiantes"),
    path("curso_formulario", curso_formulario, name="curso_formulario"),
]