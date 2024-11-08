from django.urls import path
from .views import MedicoView

urlpatterns = [
    path("", MedicoView.as_view(), name="Medico"),
]
