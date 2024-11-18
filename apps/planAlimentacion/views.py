from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ..cliente.models import Cliente
from ..usuario.mixins import ClienteRequiredMixin


# Create your views here.
class MealPlansView(LoginRequiredMixin, TemplateView):

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.is_authenticated
        return context

    def get_template_names(self):
        cliente = self.request.user.cliente
        if cliente.plan_alimentacion_id == 1:
            return ["planAlimentacion/vegetariana.html"]
        elif cliente.plan_alimentacion_id == 2:
            return ["planAlimentacion/vegana.html"]
        else:
            return ["planAlimentacion/proteica.html"]

    """ def get_template_names(self):
        cliente = self.request.user.cliente
        if cliente.vegetarian:
            return ["planAlimentacion/vegetariana.html"]
        elif cliente.vegan or (
            (cliente.hypertension or cliente.diabetic)
            and not (cliente.hypertension and cliente.diabetic)
        ):
            return ["planAlimentacion/vegana.html"]
        else:
            return ["planAlimentacion/proteica.html"] """


class ProteicaView(LoginRequiredMixin, TemplateView):
    template_name = "planAlimentacion/proteica.html"


class VeganaView(LoginRequiredMixin, TemplateView):
    template_name = "planAlimentacion/vegana.html"


class VegetarianaView(LoginRequiredMixin, TemplateView):
    template_name = "planAlimentacion/vegetariana.html"
