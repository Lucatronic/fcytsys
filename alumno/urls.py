from django.urls import path

from .views import AlumnoListado, DetalleAlumno, AlumnoActualizar

urlpatterns = [
    path('alumno/', AlumnoListado.as_view(template_name = "alumno/index.html"), name='listaAlumno'),
    path('alumno/detalle/<str:pk>', DetalleAlumno.as_view(template_name = "alumno/detalles.html"), name='detallesAlumno'),
    path('alumno/editar/<str:pk>', AlumnoActualizar.as_view(template_name = "alumno/actualizar.html"), name='actualizarAlumno'),


]