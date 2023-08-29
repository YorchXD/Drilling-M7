from django.urls import path
from . import views

urlpatterns = [
    path('laboratorios', views.laboratorio_list, name='laboratorios'),
    path('laboratorios/editar/<int:laboratorio_id>/', views.editar_laboratorio, name='editar_laboratorio'),
    path('laboratorios/eliminar/<int:laboratorio_id>/', views.confirmar_eliminar_laboratorio, name='confirmar_eliminar_laboratorio'),
    path('laboratorios/eliminar/<int:laboratorio_id>/confirmar/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
    path('laboratorios/crear/', views.crear_laboratorio, name='crear_laboratorio'),

    #path('detalle/<int:pk>/', views.detalle, name='detalle'),
]