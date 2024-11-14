from django.views.generic import TemplateView
from .models import Conversacion, Mensaje
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ChatTest(LoginRequiredMixin, TemplateView):
    template_name = "conversacion/test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        conversation_id = self.kwargs.get("conversation_id")
        conversation = get_object_or_404(Conversacion, id=conversation_id)

        context["conversation"] = conversation
        context["room_name"] = conversation_id
        context["messages"] = Mensaje.objects.filter(
            conversation=conversation
        ).order_by("created")

        return context
