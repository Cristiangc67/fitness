from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class MedicoRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, "medico"):
            raise PermissionDenied(
                "No tienes permisos para acceder a esta página no eres un medico."
            )
        return super().dispatch(request, *args, **kwargs)


class ClienteRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, "cliente"):
            raise PermissionDenied(
                "No tienes permisos para acceder a esta página no eres un cliente."
            )
        return super().dispatch(request, *args, **kwargs)
