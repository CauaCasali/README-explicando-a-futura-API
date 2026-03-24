from django.db import models

class Tarefa(models.Model):
    status_choices = [
        ("ABERTA", "Aberta"),
        ("EM_ANDAMENTO", "Em andamento"),
        ("CONCLUIDA", "Concluída"),
        ("CANCELADA", "Cancelada")
    ]
    
    prioridade_choices = [
        ("URGENTE", "Urgente"),
        ("NAO_URGENTE", "Não urgente")
    ]
    
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()   
    prioridade = models.CharField(max_length=15, choices=prioridade_choices, default="NAO_URGENTE")
    status = models.CharField(max_length=20, choices=status_choices, default="ABERTA")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    
    def __str__(self):
        return self.titulo
    
