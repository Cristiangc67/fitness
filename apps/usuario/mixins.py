from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from ..medico.models import Medico


class MedicoRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, "medico"):
            raise PermissionDenied("No tienes permisos para acceder a esta página.")
        return super().dispatch(request, *args, **kwargs)
