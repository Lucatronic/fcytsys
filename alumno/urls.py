from django.urls import path

from .views import AlumnoListado, DetalleAlumno, AlumnoActualizar

urlpatterns = [
    path('', AlumnoListado.as_view(template_name = "alumno/index.html"), name='listaAlumno'),
    path('detalle/<str:pk>', DetalleAlumno.as_view(template_name = "alumno/detalles.html"), name='detallesAlumno'),
    path('editar/<str:pk>', AlumnoActualizar.as_view(template_name = "alumno/actualizar.html"), name='actualizarAlumno'),


]