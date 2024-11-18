from django.shortcuts import render
from django.views.generic import TemplateView
from ..usuario.mixins import ClienteRequiredMixin


# Create your views here.
class PlanEjercicioView(ClienteRequiredMixin, TemplateView):
    template_name = "ejercicios.html"
