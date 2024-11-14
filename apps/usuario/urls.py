from django.urls import path
from .views import UserView, UserUpdateView

urlpatterns = [
    path("<int:pk>/", UserView.as_view(), name="perfil"),
    path("<int:pk>/editar/", UserUpdateView.as_view(), name="editar_perfil"),
]
