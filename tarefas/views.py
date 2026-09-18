from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TarefaForm
from .models import Tarefa


@login_required
def listar_tarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user)
    filtro = request.GET.get('status', '')
    if filtro == 'pendentes':
        tarefas = tarefas.filter(concluida=False)
    elif filtro == 'concluidas':
        tarefas = tarefas.filter(concluida=True)
    return render(request, 'tarefas/listar_tarefas.html',
                  {'tarefas': tarefas, 'filtro': filtro})


@login_required
def criar_tarefa(request):
    form = TarefaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        tarefa = form.save(commit=False)
        tarefa.usuario = request.user
        tarefa.save()
        messages.success(request, 'Tarefa criada com sucesso!')
        return redirect('listar_tarefas')
    return render(request, 'tarefas/criar_tarefa.html',
                  {'form': form, 'titulo_pagina': 'Nova Tarefa'})


@login_required
def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tarefa atualizada!')
        return redirect('listar_tarefas')
    return render(request, 'tarefas/criar_tarefa.html',
                  {'form': form, 'titulo_pagina': 'Editar Tarefa'})


@login_required
def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída.')
        return redirect('listar_tarefas')
    return render(request, 'tarefas/confirmar_exclusao.html', {'tarefa': tarefa})


@login_required
@require_POST
def alternar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect(request.META.get('HTTP_REFERER') or 'listar_tarefas')