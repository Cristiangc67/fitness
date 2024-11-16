from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class MealPlansView(LoginRequiredMixin, TemplateView):
    template_name = "planAlimentacion/mealPlans.html"

class ProteicaView(LoginRequiredMixin, TemplateView):
    template_name = "planAlimentacion/proteica.html"

class VeganaView(LoginRequiredMixin, TemplateView):
    template_name = "planAlimentacion/vegana.html"

class VegetarianaView(LoginRequiredMixin, TemplateView):
    template_name = "planAlimentacion/vegetariana.html"