from django.views.generic import TemplateView
from .models import Conversacion, Mensaje
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from ..cliente.models import Cliente
from ..medico.models import Medico


# Create your views here.
class ChatTest(LoginRequiredMixin, TemplateView):
    template_name = "conversacion/test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.is_authenticated
        user = self.request.user
        context[user] = user
        conversation_id = self.kwargs.get("conversation_id")
        conversation = get_object_or_404(Conversacion, id=conversation_id)
        user_id = self.request.user.id
        context["user_logged_in_id"] = user_id
        if user_id != conversation.client_id and user_id != conversation.doctor_id:
            raise PermissionDenied("No puedes editar el perfil de otro usuario.")
        else:
            context["conversation"] = conversation
            context["room_name"] = conversation_id
            context["doctor"] = get_object_or_404(Medico, id=conversation.doctor_id)
            print(context["doctor"])
            context["client"] = get_object_or_404(Cliente, id=conversation.client_id)
            print(context["client"])
            context["messages"] = Mensaje.objects.filter(
                conversation=conversation
            ).order_by("created")

        return context
