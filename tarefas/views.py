from django.shortcuts import render

def listar_tarefas(request):
    return render(request, 'tarefas/listar_tarefas.html')

def criar_tarefa(request):
    return render(request, 'tarefas/criar_tarefa.html')
