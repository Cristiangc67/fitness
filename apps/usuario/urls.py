from django.urls import path
from .views import UserView, UserUpdateView, PacientsView

urlpatterns = [
    path("<int:pk>/", UserView.as_view(), name="perfil"),
    path("<int:pk>/editar/", UserUpdateView.as_view(), name="editar_perfil"),
    path("<int:pk>/pacientes/", PacientsView.as_view(), name="medico-pacientes"),
]
