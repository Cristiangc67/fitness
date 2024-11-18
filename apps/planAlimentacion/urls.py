from django.urls import path
from .views import (
    MealPlansView,
)

urlpatterns = [
    path("", MealPlansView.as_view(), name="MealPlans"),
]
