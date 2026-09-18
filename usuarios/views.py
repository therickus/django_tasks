from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import CadastroForm


def cadastrar_usuario(request):
    if request.user.is_authenticated:
        return redirect('listar_tarefas')
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('listar_tarefas')
    else:
        form = CadastroForm()
    return render(request, 'usuarios/cadastrar_usuario.html', {'form': form})