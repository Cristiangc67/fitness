from django.views.generic import DetailView, UpdateView, TemplateView
from django.shortcuts import get_object_or_404
from .models import Usuario
from ..cliente.models import Cliente
from django.core.exceptions import PermissionDenied
from .forms.profileForm import ClienteProfileForm, MedicoProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import MedicoRequiredMixin
from ..conversacion.models import Conversacion
from django.db.models import Q
from django.core.exceptions import PermissionDenied


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


class PacientsView(MedicoRequiredMixin, TemplateView):
    template_name = "usuario/pacients.html"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.is_authenticated
        logued_in_medic = self.request.user.medico
        medico_pk = self.kwargs.get("pk")
        print(medico_pk)
        print(logued_in_medic.pk)
        if logued_in_medic.pk != medico_pk:
            raise PermissionDenied(
                "No tienes permiso para ver esta lista de pacientes."
            )

        search_query = self.request.GET.get("search", "").strip()
        clientes = Cliente.objects.filter(assigned_medico=logued_in_medic)
        if search_query:
            search_terms = search_query.split()
            query = Q()
            for term in search_terms:
                query |= Q(name__icontains=term) | Q(last_name__icontains=term)
            clientes = clientes.filter(query)
            """ clientes = clientes.filter(
                Q(name__icontains=search_query) | Q(last_name__icontains=search_query)
            ) """

        clientes_list = []
        for cliente in clientes:
            cliente.conversacion = Conversacion.objects.filter(
                client=cliente, doctor=logued_in_medic
            ).first()
            clientes_list.append(cliente)
        context["clientes"] = clientes_list
        context["search_query"] = search_query
        return context
