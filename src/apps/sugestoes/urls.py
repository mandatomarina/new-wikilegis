from django.urls import path
from .views import ProjetoCreateView, ObrigadoView

urlpatterns = [
    path('create/', ProjetoCreateView.as_view(),
         name="projeto-create"),
    path('obrigado/', ObrigadoView.as_view(), name="obrigado")
]