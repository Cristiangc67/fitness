from django.contrib import admin
from .models import Cliente
from .forms.form import ClienteCreationForm
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class ClienteAdmin(UserAdmin):
    # Campos que se mostrarán en la lista de clientes
    add_form = ClienteCreationForm
    form = ClienteCreationForm
    model = Cliente
    list_display = ("username", "email", "name", "last_name", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "name",
                    "last_name",
                    "email",
                    "weight",
                    "height",
                    "vegetarian",
                    "hypertension",
                    "diabetic",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    """ list_display = [
        "username",
        "email",
        "name",
        "last_name",
        "weight",
        "height",
        "vegetarian",
        "hypertension",
        "diabetic",
    ] """

    # Campos que se podrán editar al crear o modificar un cliente
    """ search_fields = [
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
    ] """

    # Para que los campos de contraseña y otros campos relevantes estén disponibles en el formulario de creación
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
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
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(Cliente, ClienteAdmin)
