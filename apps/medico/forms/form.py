# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models import Medico


class MedicoCreationForm(UserCreationForm):
    class Meta:
        model = Medico
        fields = (
            "username",
            "name",
            "last_name",
            "email",
            "license_number",
            "specialty",
            "previous_experience",
        )
