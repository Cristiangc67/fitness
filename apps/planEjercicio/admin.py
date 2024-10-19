from django.contrib import admin
from .models import PlanEjercicio


# Register your models here.
@admin.register(PlanEjercicio)
class planEjercicioAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "modificated", "delete"]
    search_fields = ["name", "created", "modificated", "delete"]
    list_filter = ["created", "modificated", "delete"]
