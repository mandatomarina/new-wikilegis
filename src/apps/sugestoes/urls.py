from django.urls import path
from .views import ProjetoCreateView, ObrigadoView, ProjetoList, ProjetoView, ProjetoVote, ProjetoDelete

urlpatterns = [
    path('', ProjetoList.as_view(), name="lista"),
    path('create/', ProjetoCreateView.as_view(),
         name="projeto-create"),
    path('obrigado/', ObrigadoView.as_view(), name="obrigado"),
    path('projeto/<int:projeto_id>', ProjetoView.as_view(), name="projeto"),
    path('projeto/vote/<int:projeto_id>/<str:vote>/', ProjetoVote.as_view(), name="vote"),
    path('delete/<int:pk>', ProjetoDelete.as_view(), name='projeto-delete')
]