from django.shortcuts import render
from django.views.generic import TemplateView
from ..usuario.mixins import ClienteRequiredMixin


# Create your views here.
class PlanEjercicioView(ClienteRequiredMixin, TemplateView):
    template_name = "ejercicios.html"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.is_authenticated
        user = self.request.user
        context[user] = user
        return context
