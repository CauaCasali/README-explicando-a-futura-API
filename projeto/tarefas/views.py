from django.http import JsonResponse
from django.utils import timezone
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values(
        'id', 'titulo', 'descricao', 'data_criacao',
        'usuario__username'
    )
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_por_prioridade(request, prioridade):
    tarefas = Tarefa.objects.filter(prioridade=prioridade).values()
    return JsonResponse(list(tarefas), safe=False)

def buscar_tarefa_por_id(request, id):
    try:
        tarefa = Tarefa.objects.get(id=id)
        return JsonResponse({
            'id': tarefa.id,
            'titulo': tarefa.titulo,
            'descricao': tarefa.descricao,
            'prioridade': tarefa.prioridade,
            'status': tarefa.status,
            'data_criacao': tarefa.data_criacao,
            'data_entrega': tarefa.data_entrega
        })
    except Tarefa.DoesNotExist:
        return JsonResponse({
            'erro': 'Tarefa não encontrada',
            'id': id
        }, status=404)

def listar_tarefas_abertas_urgentes(request):
    tarefas = Tarefa.objects.filter(
        status='ABERTA',
        prioridade='URGENTE'
    ).values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_atrasadas(request):
    hoje = timezone.now().date()
    tarefas = Tarefa.objects.filter(
        data_entrega__lt=hoje
    ).exclude(status='CONCLUIDA').values()
    return JsonResponse(list(tarefas), safe=False)

def buscar_tarefas_por_palavra(request, palavra):
    tarefas = Tarefa.objects.filter(
        titulo__icontains=palavra
    ).values()
    return JsonResponse(list(tarefas), safe=False)

# Create your views here.
