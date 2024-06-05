from django.urls import path
from . import views

urlpatterns = [
    # URLs de vistas normales
    path('', views.listar_productos, name='listar_productos'),
    path('agregar/', views.agregar_productos, name='agregar_productos'),
    path('eliminar/<id>', views.eliminar_producto, name='eliminar_producto'),
    path('editar/<id>', views.editar_producto, name='editar_producto'),
]