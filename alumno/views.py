from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
from .models import Alumno, Institucion


#========================== ALUMNO =======================================

class AlumnoListado(LoginRequiredMixin, ListView):
    model = Alumno
    extra_context = {'titulo': 'Alumno',
                     'plural': 'Alumnos'}


class AlumnoActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Alumno
    form = Alumno
    fields = ['nombre', 'apellidos', 'institucion']
    success_message = 'Alumno Actualizado Correctamente !'
    extra_context = {'titulo': 'Editar Alumno'}

    def get_success_url(self):
        return reverse('listaAlumno')


#========================== INSTITUCIÓN =======================================
class InstitucionListado(LoginRequiredMixin, ListView):
    model = Institucion
    extra_context = {'titulo': 'Institución',
                     'plural': 'Instituciones'}
