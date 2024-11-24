from . import views
from django.urls import path

app_name = 'vehiculo'
urlpatterns = [
    # path('', views.index, name='vehiculo_index'),
    path('add/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('listar/', views.listar, name='listar'),
]
