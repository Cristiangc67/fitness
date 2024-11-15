# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models import Cliente


class ClienteCreationForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = (
            "username",
            "name",
            "last_name",
            "email",
            "weight",
            "height",
            "vegetarian",
            "hypertension",
            "diabetic",
            "others",
        )
