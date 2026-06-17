from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('disciplinas/adicionar/', views.adicionar_disciplina, name='adicionar_disciplina'),
    path('disciplinas/<int:pk>/remover/', views.remover_disciplina, name='remover_disciplina'),
    path('avaliacoes/adicionar/', views.adicionar_avaliacao, name='adicionar_avaliacao'),
    path('avaliacoes/<int:pk>/concluir/', views.concluir_avaliacao, name='concluir_avaliacao'),
]
