from django.urls import path
from .views import MealPlansView, ProteicaView, VeganaView, VegetarianaView

urlpatterns = [
    path("", MealPlansView.as_view(), name="MealPlans"),
    path("proteica/", ProteicaView.as_view(), name="Proteica"),
    path("vegana/", VeganaView.as_view(), name="Vegana"),
    path("vegetariana/", VegetarianaView.as_view(), name="Vegetariana")
]
