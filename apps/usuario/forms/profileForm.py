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
