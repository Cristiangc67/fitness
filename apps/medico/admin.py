from django.contrib import admin
from .models import Medico
from .forms.form import MedicoCreationForm
from django.contrib.auth.admin import UserAdmin


class MedicoAdmin(UserAdmin):
    add_form = MedicoCreationForm
    form = MedicoCreationForm
    model = Medico
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
                    "license_number",
                    "specialty",
                    "previous_experience",
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
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "name",
                    "last_name",
                    "email",
                    "license_number",
                    "specialty",
                    "previous_experience",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(Medico, MedicoAdmin)
