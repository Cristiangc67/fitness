from typing import Any
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView
from apps.medico.models import Medico
from apps.main.forms import MedicoForms
from apps.cliente.models import Cliente
from apps.main.forms import ClienteForms
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.conf import settings  


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

    def get(self, request):
        # Renderiza la página de inicio de sesión
        return self.render_to_response({})

    def post(self, request):
        # Procesa el inicio de sesión
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Autenticación utilizando el email como 'username'
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Inicia sesión al usuario
            return redirect(settings.LOGIN_REDIRECT_URL)  # Redirige a la URL de inicio después de loguearse
        else:
            # Si las credenciales son incorrectas, redirige al login con un mensaje de error
            return redirect(f"{settings.LOGIN_URL}?error=Credenciales inválidas")
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
    template_name = "main/registration/registerClient.html"
    success_url = reverse_lazy("Login")
    
class RegisterMedicView(CreateView):
    model = Medico
    form_class = MedicoForms
    template_name = "main/registration/registerMedic.html"
    success_url = reverse_lazy("Login")