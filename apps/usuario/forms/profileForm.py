from django import forms
from apps.medico.models import Medico
from apps.cliente.models import Cliente
from apps.planAlimentacion.models import PlanAlimentacion
from apps.planEjercicio.models import PlanEjercicio

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
    plan_alimentacion = forms.ModelChoiceField(
        queryset=PlanAlimentacion.objects.all(), 
        required=False, 
        label="Seleccionar Nuevo Plan de Alimentación"
    )
    plan_ejercicio = forms.ModelChoiceField(
        queryset=PlanEjercicio.objects.all(), 
        required=False, 
        label="Seleccionar Nuevo Plan de Ejercicio"
    )

    class Meta:
        model = Cliente
        fields = ['sugerencias']
        widgets = {
            'sugerencias': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Escribe comentarios específicos para el plan...',
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añade la clase form-control a los campos de selección
        self.fields['plan_alimentacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['plan_ejercicio'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True, medico=None):
        cliente = super().save(commit=False)
        
        if medico:
            # Asegurarse de que los planes sugeridos sean solo para este cliente
            if self.cleaned_data.get('plan_alimentacion'):
                cliente.plan_alimentacion = self.cleaned_data['plan_alimentacion']
            
            if self.cleaned_data.get('plan_ejercicio'):
                cliente.plan_ejercicio = self.cleaned_data['plan_ejercicio']
        
        if commit:
            cliente.save()
        return cliente