from django import forms
from .models import Alumno
from django.forms.models import ModelForm
from django.forms.widgets import Select

class AlumnoForm(ModelForm):

    class Meta:
        model = Alumno
        fields = ['institucion']

        # widgets = {
        #     'institucion': Select(),
        # }
