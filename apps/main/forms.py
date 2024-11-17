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
        widgets = {
            'password': forms.PasswordInput()  # Para que se muestre como campo password
        }
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hashea la contraseña
        if commit:
            user.save()
        return user
        
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
        widgets = {
            'password': forms.PasswordInput()  # Para que se muestre como campo password
        }
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hashea la contraseña
        if commit:
            user.save()
        return user