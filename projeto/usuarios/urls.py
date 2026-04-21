from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', views.listar_usuarios, name='listar_usuarios'),
    path('usuario/<int:id>/', views.buscar_usuario_por_id, name='buscar_usuario_por_id'),
]