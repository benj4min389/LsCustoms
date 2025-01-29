from django.urls import path
from . import views


urlpatterns = [
    path('',views.principal , name="main"),
    path('todasreparaciones',views.todas_reparaciones, name="todasreparaciones"),
    path('todasreparaciones/<int:id>',views.detalle_reparacion, name="detallerep"),
    path('crear-miembro', views.crear_miembro, name="crear_miembro"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('registro', views.registro, name='registro'),
   
]