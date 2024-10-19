from django.contrib import admin
from .models import Medico


# Register your models here.
@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de médicos
    list_display = [
        "username",
        "email",
        "name",
        "last_name",
        "license_number",
        "specialty",
    ]

    # Campos que se podrán editar al crear o modificar un médico
    search_fields = [
        "username",
        "password",
        "email",
        "name",
        "last_name",
        "license_number",
        "specialty",
        "previous_experience",
        "delete",
    ]

    # Configuración para ingresar la contraseña y otros datos relevantes en el formulario de creación
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password",
                    "email",
                    "name",
                    "last_name",
                    "licenseNumber",
                    "specialty",
                    "previous_experience",
                ),
            },
        ),
    )
