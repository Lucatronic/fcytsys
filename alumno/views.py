from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
from .models import Alumno, Institucion
from .forms import AlumnoForm


#========================== ALUMNO =======================================

class AlumnoListado(LoginRequiredMixin, ListView):
    model = Alumno
    extra_context = {'titulo': 'Alumno',
                     'plural': 'Alumnos'}


class AlumnoDetalle(LoginRequiredMixin, DetailView):
    model = Alumno
    extra_context = {'titulo': 'Detalles del Alumno'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        institucion = Institucion.objects.all().values('id', 'nombre_institucion', 'niveles_modalidades', 'nombre_distrito')
        context.update(locals())
        return context

class DetalleAlumno(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Alumno
    form = Alumno
    fields = ['institucion']
    success_message = 'Alumno Actualizado Correctamente !'
    extra_context = {'titulo': 'Actualizar Alumno'}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alumno = Alumno.objects.get(id=self.kwargs['pk'])
        institucion = Institucion.objects.all().values('id', 'nombre_institucion', 'niveles_modalidades', 'nombre_distrito')
        context.update(locals())
        return context
    
    def get_success_url(self):
        alumno = Alumno.objects.get(id=self.kwargs['pk'])
        return reverse('detallesAlumno', args=[self.kwargs['pk'],])


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
