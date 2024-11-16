from django import forms
from apps.medico.models import Medico
from apps.cliente.models import Cliente


class MedicoForms(forms.ModelForm):
    
    class Meta:
        model = Medico
        fields = [
            "name",
            "last_name",
            "username",
            "email",
            "password",
            "license_number",
            "specialty",
            "previous_experience",
        ]
        
class ClienteForms(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = [
            "name",
            "last_name",
            "username",
            "email",
            "weight",
            "height",
            "genre",
            "password",
            "vegetarian",
            "hypertension",
            "diabetic",
            "others",
        ]