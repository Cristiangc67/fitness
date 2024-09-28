from django.db import models
from apps.usuario.models import Usuario


# Create your models here.
class Cliente(Usuario):
    weight = models.DecimalField(max_digits=3, decimal_places=2)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    vegetarian = models.BooleanField()
    hypertension = models.BooleanField()
    diabetic = models.BooleanField()
    others = models.CharField(max_length=500)
    planAlimentacion = models.ForeignKey(
        "planAlimentacion.PlanAlimentacion", on_delete=models.CASCADE
    )
    planEjercicio = models.ForeignKey(
        "planEjercicio.PlanEjercicio", on_delete=models.CASCADE
    )
