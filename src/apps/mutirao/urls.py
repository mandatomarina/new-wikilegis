from django.urls import path
from .views import MutiraoView, MutiraoRnd

urlpatterns = [
    path('<str:tipo>/<int:numero>/<int:ano>', MutiraoRnd.as_view(), name="mutirao_rnd"),
    path('<str:tipo>/<int:numero>/<int:ano>/emenda/<int:numero_emenda>/<int:ano_emenda>', MutiraoView.as_view(), name="mutirao")
]