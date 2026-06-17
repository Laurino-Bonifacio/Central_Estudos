from django.db import models


class Avaliacao(models.Model):
    titulo = models.CharField(max_length=100)
    data_prova = models.DateField()
    conteudo = models.TextField(blank=True, null=True)
    estudo_concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
