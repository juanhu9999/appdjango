from django import forms

class curso_formulario(forms.form):

    curso = forms.CharField()
    camada = forms.IntegerField()