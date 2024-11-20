from django import forms
from apps.medico.models import Medico
from apps.cliente.models import Cliente


class ClienteProfileForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            "username",
            "email",
            "weight",
            "height",
            "vegetarian",
            "hypertension",
            "diabetic",
        ]


class MedicoProfileForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = [
            "name",
            "last_name",
            "username",
            "email",
            "license_number",
            "specialty",
            "previous_experience",
        ]


class SugerenciaPlanForm(forms.ModelForm):
    PLAN_ALIMENTACION_CHOICES = [
        (1, "Vegetariana"),
        (2, "Vegana"),
        (3, "Proteica"),
    ]
    plan_alimentacion = forms.ChoiceField(
        choices=PLAN_ALIMENTACION_CHOICES,
        required=False,
        label="Seleccionar Nuevo Plan de Alimentación",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Cliente
        fields = ["sugerencias"]
        widgets = {
            "sugerencias": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Escribe comentarios específicos para el plan...",
                    "class": "form-control",
                }
            )
        }

    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop("cliente", None)
        super().__init__(*args, **kwargs)

        # Establecer el valor inicial de plan_alimentacion si el cliente ya tiene uno asignado
        if cliente and cliente.plan_alimentacion:
            self.fields["plan_alimentacion"].initial = cliente.plan_alimentacion

        # Añadir la clase form-control a los campos de selección
        self.fields["plan_alimentacion"].widget.attrs.update({"class": "form-control"})

    def save(self, commit=True, medico=None):
        cliente = super().save(commit=False)

        if medico:
            # Asegurarse de que los planes sugeridos sean solo para este cliente
            if self.cleaned_data.get("plan_alimentacion"):
                cliente.plan_alimentacion = self.cleaned_data["plan_alimentacion"]

        if commit:
            cliente.save()
        return cliente
