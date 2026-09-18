from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('nova/', views.criar_tarefa, name='criar_tarefa'),
    path('<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('<int:pk>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
    path('<int:pk>/alternar/', views.alternar_tarefa, name='alternar_tarefa'),
]