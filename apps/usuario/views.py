from django.views.generic import DetailView, UpdateView, ListView
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Usuario
from ..cliente.models import Cliente
from ..medico.models import Medico
from django.core.exceptions import PermissionDenied
from .forms.profileForm import ClienteProfileForm, MedicoProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import MedicoRequiredMixin, ClienteRequiredMixin
from ..conversacion.models import Conversacion
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.db.models import Count


# Create your views here.
class UserView(DetailView):

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

    def get_template_names(self):

        user = self.get_object()
        if hasattr(user, "cliente"):
            return ["usuario/clienteProfile.html"]
        elif hasattr(user, "medico"):
            return ["usuario/medicoProfile.html"]
        else:
            return ["usuario/userProfile.html"]


class UserUpdateView(UpdateView):
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

    def get_template_names(self):

        user = self.get_object()
        if hasattr(user, "cliente"):
            return ["usuario/clienteProfileEdit.html"]
        elif hasattr(user, "medico"):
            return ["usuario/medicoProfileEdit.html"]
        else:
            return ["usuario/userProfileEdit.html"]


class PacientsView(MedicoRequiredMixin, ListView):
    model = Cliente
    template_name = "usuario/pacients.html"
    context_object_name = "clientes"
    paginate_by = 10

    def get_queryset(self):
        logued_in_medic = self.request.user.medico
        medico_pk = self.kwargs.get("pk")

        if logued_in_medic.pk != medico_pk:
            raise PermissionDenied(
                "No tienes permiso para ver esta lista de pacientes."
            )

        clientes = Cliente.objects.filter(assigned_medico=logued_in_medic)

        search_query = self.request.GET.get("search", "").strip()
        if search_query:
            search_terms = search_query.split()
            query = Q()
            for term in search_terms:
                query |= Q(name__icontains=term) | Q(last_name__icontains=term)
            clientes = clientes.filter(query)

        for cliente in clientes:
            cliente.conversacion = Conversacion.objects.filter(
                client=cliente, doctor=logued_in_medic
            ).first()

        return clientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.is_authenticated
        context["search_query"] = self.request.GET.get("search", "").strip()
        return context


class ClienteChatRedirectView(ClienteRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):

        cliente = get_object_or_404(Cliente, pk=pk)

        if not cliente.assigned_medico_id:

            assigned_medico = (
                Medico.objects.annotate(num_pacientes=Count("cliente"))
                .order_by("num_pacientes")
                .first()
            )
            print(assigned_medico)
            if not assigned_medico:

                print("fallo")
                return redirect("perfil", pk=pk)

            cliente.assigned_medico_id = assigned_medico.id
            cliente.save()

        conversacion, created = Conversacion.objects.get_or_create(
            client_id=cliente.id,
            doctor_id=cliente.assigned_medico_id,
            created_by_id=cliente.id,
        )

        return redirect(reverse("chatTest", args=[conversacion.pk]))
