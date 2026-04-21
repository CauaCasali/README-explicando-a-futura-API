from django.http import JsonResponse
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all().values()
    return JsonResponse(list(usuarios),safe=False)

def buscar_usuario_por_id(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        return JsonResponse({
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email,
            'ativo': usuario.ativo,
            'data_criacao': usuario.data_criacao,
        })
    except Usuario.DoesNotExist:
        return JsonResponse({
            'erro': 'Usuario não encontrada',
            'id': id
        }, status=404)

    
# Create your views here.
