from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    model = models.Projeto

@admin.register(models.Tema)
class TemaAdmin(admin.ModelAdmin):
    model = models.Tema

@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    model = models.Status

