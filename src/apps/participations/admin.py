from django.contrib import admin

from .models import InvitedGroup, Suggestion, OpinionVote
from import_export.admin import  ImportExportModelAdmin
from import_export import resources


@admin.register(InvitedGroup)
class InvitedGroupAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'document',
        'thematic_group',
        'closing_date',
        'public_participation',
    )
    list_filter = (
        'created',
        'modified',
        'closing_date',
        'public_participation',
    )

    search_fields = ('thematic_group__name',
                     'document__title')

class SuggestionResource(resources.ModelResource):
    class Meta:
        model = Suggestion
        fields = ('author__email', 'author__profile__full_name', 'author__profile__gender', 'author__profile__elector', 'author__profile__uf', 'author__profile__phone')

@admin.register(Suggestion)
class SuggestionAdmin(ImportExportModelAdmin):
    resource_class =  SuggestionResource
    list_display = (
        'id',
        'created',
        'modified',
        'invited_group',
        'content',
        'author',
    )
    list_filter = (
        'created',
        'modified',
        'invited_group__document__title',
    )
    search_fields = ('invited_group__thematic_group__name',
                     'author__first_name', 'content')


@admin.register(OpinionVote)
class OpinionVoteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'suggestion',
        'owner',
        'opinion_vote',
    )
    list_filter = ('created', 'modified')
    search_fields = ('owner__first_name', 'suggestion__content')
