from django.urls import path
from .views import MutiraoView

urlpatterns = [
    path('<str:tipo>/<int:numero>/<int:ano>', MutiraoView.as_view(), name="mutirao"),
]