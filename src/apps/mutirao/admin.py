from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from . import models

# Register your models here.
@admin.register(models.Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    model = models.Projeto

class EmendaResource(resources.ModelResource):
    class Meta:
        model = models.Emenda

class EmendaAdmin(ImportExportModelAdmin):
    resource_class= EmendaResource

class ReviewResource(resources.ModelResource):
    class Meta:
        model = models.Review

class ReviewAdmin(ImportExportModelAdmin):
    resource_class = ReviewResource

admin.site.register(models.Review, ReviewAdmin)
admin.site.register(models.Emenda, EmendaAdmin)