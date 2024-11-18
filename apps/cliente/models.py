from django.db import models
from apps.usuario.models import Usuario


# Create your models here.
class Cliente(Usuario):
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    genre = models.CharField(  # Ahora definido correctamente
        max_length=10,
        choices=[("Masculino", "Masculino"), ("Femenino", "Femenino")],
        blank=True,
        null=True,
    )
    vegetarian = models.BooleanField(default=False)
    hypertension = models.BooleanField(default=False)
    diabetic = models.BooleanField(default=False)
    others = models.CharField(max_length=500, blank=True, null=True)
    plan_alimentacion = models.ForeignKey(
        "planAlimentacion.PlanAlimentacion",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    plan_ejercicio = models.ForeignKey(
        "planEjercicio.PlanEjercicio", on_delete=models.CASCADE, blank=True, null=True
    )
    assigned_medico = models.ForeignKey(
        "medico.Medico", on_delete=models.CASCADE, null=True, blank=True
    )
