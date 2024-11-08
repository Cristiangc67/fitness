from django.shortcuts import render
from django.views.generic import TemplateView
from apps.usuario.models import Usuario
from apps.medico.models import Medico


# Create your views here.
class MedicoView(TemplateView):
    template_name = "medico/medico.html"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        id_medico = self.request.GET.get("id_medico")
        context["medicos"] = Medico.objects.filter(id=int(id_medico))
        print(context["medicos"])
        return context
