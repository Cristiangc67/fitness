from typing import Any
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView
from apps.medico.models import Medico
from apps.main.forms import MedicoForms
from apps.cliente.models import Cliente
from apps.main.forms import ClienteForms

# Create your views here.
class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.is_authenticated
        return context


class AboutUsView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.is_authenticated
        return context


class LogInView(TemplateView):
    template_name = "main/login.html"
    
class RegisterTemplateMedicView(TemplateView):
    template_name = "main/registration/registerMedic.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["medicos"] = Medicos.objects.all()
        return context
    
class RegisterTemplateClientView(TemplateView):
    template_name = "main/registration/registerClient.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["clientes"] = Clientes.objects.all()
    
class RegisterClientView(CreateView):
    model = Cliente
    form_class = ClienteForms
    success_url = reverse_lazy("Home")
    
class RegisterMedicView(CreateView):
    model = Medico
    form_class = MedicoForms
    template_name = "main/registration/registerMedic.html"
    success_url = reverse_lazy("Home")