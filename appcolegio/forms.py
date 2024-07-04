from django import forms
from django.forms import ModelForm
from.models import CursoMateria


class cargarcurso(forms.Form):
    curso = forms.CharField()
    division = forms.CharField()
    profesor = forms.CharField()

class buscarCursos(forms.Form):
    curso = forms.CharField()

class BuscaCursoForm(forms.Form):
    curso = forms.CharField()

class cargarprof(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    email = forms.EmailField()

class cargarestu(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    email = forms.EmailField()

class cargarmateria(forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()
    profesor = forms.CharField()

class RegistroForm(forms.Form):
    class Meta:
        model = CursoMateria
        fields = ['cursos','materia']
   