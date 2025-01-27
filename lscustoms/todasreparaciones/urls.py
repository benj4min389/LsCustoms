from django.urls import path
from . import vistas


urlpatterns = [
    path(''vistas.main, name="main"),
    path('todasreparaciones/detallerep/<int:id>',vistas.detalle_reparacion, name="detallerep"),
    path
]