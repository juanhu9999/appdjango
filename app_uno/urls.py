from django.urls import path
from app_uno.views import inicio, cursos, estudiantes

urlpatterns = [
    path('', inicio, name="inicio"),
    path('cursos', cursos,name="cursos"),
    path('estudiantes', estudiantes, name="estudiantes"),

]