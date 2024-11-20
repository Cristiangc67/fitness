from django.urls import path
from .views import PlanEjercicioView

urlpatterns = [
    path("", PlanEjercicioView.as_view(), name="PlanEjercicio")
]