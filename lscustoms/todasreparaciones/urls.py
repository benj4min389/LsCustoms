from django.urls import path
from . import views


urlpatterns = [
    path('',views.principal , name="main"),
    path('todasreparaciones/detallerep/<int:id>',views.detalle_reparacion, name="detallerep"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('registro', views.registro, name='registro')
]