from django.db import models
from django.contrib.auth.models import User# Create your models here.

DEFAULT_STATUS = 1

class Tema(models.Model):
    nome = models.CharField('Nome', max_length=200)

    def __str__(self):
        return(self.nome)

class Status(models.Model):
    nome = models.CharField('Nome', max_length=200)

    def __str__(self):
        return(self.nome)

class Projeto(models.Model):
    titulo = models.CharField('Titulo', max_length=140)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    ementa = models.CharField('Ementa', max_length=280)
    descritivo = models.TextField('Descritivo', max_length=500)
    justificativa = models.CharField('Justificativa', max_length=280)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=DEFAULT_STATUS)
    concordo = models.BooleanField(default=False)
    apoiador = models.ManyToManyField(User, related_name='apoiador_projeto')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autor_projeto', null=True)

    def __str__(self):
        return(self.ementa)