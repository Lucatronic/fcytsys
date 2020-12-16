from django.urls import path

from .views import AlumnoListado, AlumnoActualizar

urlpatterns = [
    path('alumno/', AlumnoListado.as_view(template_name = "alumno/index.html"), name='listaAlumno'),
    path('alumno/editar/<str:pk>', AlumnoActualizar.as_view(template_name = "alumno/actualizar.html"), name='actualizarAlumno'),


]