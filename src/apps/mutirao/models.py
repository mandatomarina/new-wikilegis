from django.db import models
from django.contrib.auth.models import User# Create your models here.

# Create your models here.
class Projeto(models.Model):
    tipo = models.CharField(max_length=4)
    numero = models.IntegerField()
    ano = models.IntegerField()
    arquivo = models.FileField(upload_to='mutirao/projetos/')

    def __str__(self):
        return self.tipo + " " + str(self.numero)+"/"+str(self.ano)


class Emenda(models.Model):
    pl = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    numero = models.IntegerField()
    ano = models.IntegerField()
    ementa = models.TextField()
    autor = models.CharField(max_length=140)
    link = models.URLField()
    arquivo = models.FileField(upload_to='mutirao/emendas/', null=True)


    def __str__(self):
        return str(self.numero)+'/'+str(self.ano) + ' - ' + self.ementa

class Review(models.Model):
    emenda = models.ForeignKey(Emenda, on_delete=models.CASCADE)
    apoiar = models.BooleanField()
    justificativa = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    