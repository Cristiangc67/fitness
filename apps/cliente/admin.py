from django.contrib import admin
from .models import Cliente


# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de clientes
    list_display = [
        "username",
        "email",
        "name",
        "last_name",
        "weight",
        "height",
        "vegetarian",
        "hypertension",
        "diabetic",
    ]

    # Campos que se podrán editar al crear o modificar un cliente
    search_fields = [
        "username",
        "email",
        "name",
        "last_name",
        "weight",
        "height",
        "vegetarian",
        "hypertension",
        "diabetic",
        "others",
        "plan_alimentacion",
        "plan_ejercicio",
        "delete",
    ]

    # Para que los campos de contraseña y otros campos relevantes estén disponibles en el formulario de creación
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
                    "weight",
                    "height",
                    "vegetarian",
                    "hypertension",
                    "diabetic",
                    "others",
                    "plan_alimentacion",
                    "plan_ejercicio",
                ),
            },
        ),
    )
