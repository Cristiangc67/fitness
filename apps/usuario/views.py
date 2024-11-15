from django.views.generic import DetailView, UpdateView, TemplateView
from django.shortcuts import get_object_or_404
from .models import Usuario
from ..cliente.models import Cliente
from django.core.exceptions import PermissionDenied
from .forms.profileForm import ClienteProfileForm, MedicoProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class UserView(DetailView):
    template_name = "usuario/userProfile.html"
    context_object_name = "perfil"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.is_authenticated
        context["user_logged_in"] = self.request.user
        context["profile_user"] = self.get_object()
        return context

    def get_object(self):
        user_pk = self.kwargs.get("pk")
        print("User PK:", user_pk)
        user = get_object_or_404(Usuario, pk=user_pk)
        print(user)
        if hasattr(user, "cliente"):
            return user.cliente
        elif hasattr(user, "medico"):
            return user.medico
        else:
            return user


class UserUpdateView(UpdateView):
    template_name = "usuario/userProfileEdit.html"
    context_object_name = "perfil"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.is_authenticated
        return context

    def get_object(self):
        user_pk = self.kwargs.get("pk")
        user = get_object_or_404(Usuario, pk=user_pk)

        if user != self.request.user:
            raise PermissionDenied("No puedes editar el perfil de otro usuario.")

        if hasattr(user, "cliente"):
            return user.cliente
        elif hasattr(user, "medico"):
            return user.medico
        else:
            return user

    def get_form_class(self):
        if hasattr(self.get_object(), "cliente"):
            return ClienteProfileForm
        elif hasattr(self.get_object(), "medico"):
            return MedicoProfileForm


class pacientsView(LoginRequiredMixin, TemplateView):
    template_name = "usuario/pacients.html"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.is_authenticated
        user_pk = self.kwargs.get("pk")
        context["clientes"] = Cliente.objects.filter(assigned_medico_id=int(user_pk))
        return context
