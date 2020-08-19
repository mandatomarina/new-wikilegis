from django.urls import path
from .views import ProjetoCreateView, ObrigadoView, ProjetoList, ProjetoView

urlpatterns = [
    path('create/', ProjetoCreateView.as_view(),
         name="projeto-create"),
    path('obrigado/', ObrigadoView.as_view(), name="obrigado"),
    path('lista/', ProjetoList.as_view(), name="lista"),
    path('projeto/<int:projeto_id>', ProjetoView.as_view(), name="projeto")
]