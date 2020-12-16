from django.contrib import admin

# Register your models here.
from .models import Alumno, Institucion

admin.site.register(Alumno)
admin.site.register(Institucion)
