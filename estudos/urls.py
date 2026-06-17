from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar'),

    # Disciplinas
    path('disciplinas/adicionar/', views.adicionar_disciplina, name='adicionar_disciplina'),
    path('disciplinas/<int:pk>/remover/', views.remover_disciplina, name='remover_disciplina'),
    path('disciplinas/<int:pk>/registrar-hora/', views.registrar_hora_estudo, name='registrar_hora_estudo'),
    path('disciplinas/resetar-ciclo/', views.resetar_ciclo, name='resetar_ciclo'),

    # Conteúdos de aula
    path('disciplinas/<int:disciplina_id>/conteudos/', views.listar_conteudos, name='listar_conteudos'),
    path('disciplinas/<int:disciplina_id>/conteudos/adicionar/', views.adicionar_conteudo, name='adicionar_conteudo'),
    path('disciplinas/<int:disciplina_id>/conteudos/remover-todos/', views.remover_todos_conteudos, name='remover_todos_conteudos'),
    path('conteudos/<int:pk>/remover/', views.remover_conteudo, name='remover_conteudo'),

    # Avaliações
    path('avaliacoes/adicionar/', views.adicionar_avaliacao, name='adicionar_avaliacao'),
    path('avaliacoes/<int:pk>/concluir/', views.concluir_avaliacao, name='concluir_avaliacao'),
    path('avaliacoes/<int:pk>/remover/', views.remover_avaliacao, name='remover_avaliacao'),
]
