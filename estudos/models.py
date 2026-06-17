from django.db import models
from django.contrib.auth.models import User


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    cor_identificacao = models.CharField(max_length=20)
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='disciplinas'
    )

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    titulo = models.CharField(max_length=100)
    data_prova = models.DateField()
    data_prazo = models.DateField(blank=True, null=True)
    conteudo = models.TextField(blank=True, null=True)
    estudo_concluido = models.BooleanField(default=False)
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='avaliacoes'
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='avaliacoes'
    )

    def __str__(self):
        return self.titulo


class MaterialEstudo(models.Model):
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='materiais/')
    data_upload = models.DateTimeField(auto_now_add=True)
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='materiais'
    )

    def __str__(self):
        return self.titulo
