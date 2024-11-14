from django.views.generic import DetailView, UpdateView
from django.shortcuts import get_object_or_404
from .models import Usuario


# Create your views here.
class UserView(DetailView):
    template_name = "usuario/userProfile.html"
    context_object_name = "perfil"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.is_authenticated
        return context

    def get_object(self):
        user_pk = self.kwargs.get("pk")
        user = get_object_or_404(Usuario, pk=user_pk)

        if hasattr(user, "cliente"):
            return user.cliente
        elif hasattr(user, "medico"):
            return user.medico
        else:
            return user


class UserUpdateView(UpdateView):
    pass
