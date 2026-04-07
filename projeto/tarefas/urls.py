from django.urls import path
from .views import (
    listar_tarefas,
    listar_tarefas_por_prioridade,
    buscar_tarefa_por_id,
    listar_tarefas_abertas_urgentes,
    listar_tarefas_atrasadas,
    buscar_tarefas_por_palavra
)


urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/<int:id>/', buscar_tarefa_por_id),
    path('tarefas/prioridade/<str:prioridade>/', listar_tarefas_por_prioridade),
    path('tarefas/abertas-urgentes/', listar_tarefas_abertas_urgentes),
    path('tarefas/atrasadas/', listar_tarefas_atrasadas),
    path('tarefas/busca/<str:palavra>/', buscar_tarefas_por_palavra),
]
