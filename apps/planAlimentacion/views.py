from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ..cliente.models import Cliente
from ..usuario.mixins import ClienteRequiredMixin



class MealPlansView(ClienteRequiredMixin, TemplateView):

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        cliente = user.cliente

        # Obtener la sugerencia del cliente
        suggestion = cliente.sugerencias

        # Obtener el médico asignado (instancia de Medico)
        medico = cliente.assigned_medico  # Esto devuelve una instancia de Medico (que es un Usuario también)

        # Verificar si existe un médico asignado
        if medico:
            # El nombre completo del médico se obtiene de los campos de Usuario heredados
            medico_nombre = f"Dr. {medico.name} {medico.last_name}"
        else:
            medico_nombre = "Sin médico asignado"

        # Agregar la sugerencia y el nombre del médico al contexto
        context["sugerencias"] = suggestion if suggestion else None
        context["medico_nombre"] = medico_nombre

        # Continuar con el contexto habitual
        context["is_authenticated"] = self.request.user.is_authenticated
        context[user] = user
        return context

    def get_template_names(self):
        cliente = self.request.user.cliente
        if cliente.plan_alimentacion_id == 1:
            return ["planAlimentacion/vegetariana.html"]
        elif cliente.plan_alimentacion_id == 2:
            return ["planAlimentacion/vegana.html"]
        else:
            return ["planAlimentacion/proteica.html"]