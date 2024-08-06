from django.urls import path
from app_uno.views import inicio, cursos, estudiantes

urlpatterns = [
    path('', inicio),
    path('cursos', cursos),
    path('estudiantes', estudiantes),

]