from django.db import models
from django.contrib.auth.models import User


class Disciplina(models.Model):
    NIVEL_CHOICES = [(i, str(i)) for i in range(1, 6)]

    nome = models.CharField(max_length=100)
    cor_identificacao = models.CharField(max_length=20)
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='disciplinas'
    )
    dificuldade = models.IntegerField(choices=NIVEL_CHOICES, default=3)
    quantidade_conteudo = models.IntegerField(choices=NIVEL_CHOICES, default=3)
    peso = models.FloatField(default=1.0)
    horas_ciclo = models.IntegerField(default=0)
    horas_concluidas = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        calculado = round((self.dificuldade + self.quantidade_conteudo) * self.peso)
        self.horas_ciclo = max(calculado, 1)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class ConteudoAula(models.Model):
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='conteudos'
    )
    titulo = models.CharField(max_length=200)
    data_registro = models.DateField()
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-data_registro', 'titulo']

    def __str__(self):
        return f"{self.disciplina.nome} — {self.titulo}"


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
    conteudos_cobrados = models.ManyToManyField(
        ConteudoAula,
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
