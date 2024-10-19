from django.contrib import admin
from .models import PlanAlimentacion


# Register your models here.
@admin.register(PlanAlimentacion)
class planAlimentacionAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "modificated", "delete"]
    search_fields = ["name", "created", "modificated", "delete"]
    list_filter = ["created", "modificated", "delete"]
