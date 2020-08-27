from django.urls import path
from .views import EmendaView, MutiraoRnd, EmendaListView

urlpatterns = [
    path('<str:tipo>/<int:numero>/<int:ano>', MutiraoRnd.as_view(), name="mutirao_rnd"),
    path('<str:tipo>/<int:numero>/<int:ano>/lista', EmendaListView.as_view(), name="lista"),
    path('<str:tipo>/<int:numero>/<int:ano>/emenda/<int:numero_emenda>/<int:ano_emenda>', EmendaView.as_view(), name="emenda")
]