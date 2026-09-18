from django.conf import settings
from django.db import models


class Tarefa(models.Model):
    PRIORIDADES = [
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADES, default='M')
    prazo = models.DateField(null=True, blank=True)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tarefas',
    )

    class Meta:
        ordering = ['concluida', '-criada_em']

    def __str__(self):
        return self.titulo