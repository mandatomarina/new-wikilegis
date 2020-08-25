from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    model = models.Projeto

@admin.register(models.Emenda)
class EmendaAdmin(admin.ModelAdmin):
    model = models.Emenda

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    model = models.Review
