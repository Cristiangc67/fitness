from django.contrib import admin
from .models import Conversacion


# Register your models here.
@admin.register(Conversacion)
class ConversacionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "client",
        "doctor",
        "created",
        "modificated",
    ]
    search_fields = [
        "client",
        "doctor",
        "created",
        "modificated",
    ]
    list_filter = ["created", "modificated", "delete", "doctor"]
