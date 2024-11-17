from django.urls import path
from .views import HomeView, AboutUsView, LogInView, RegisterClientView, RegisterMedicView

urlpatterns = [
    path("home/", HomeView.as_view(), name="Home"),
    path("about/", AboutUsView.as_view(), name="About"),
    path("login/", LogInView.as_view(), name="Login"),
    path("login/register_client/", RegisterClientView.as_view(), name="RegisterClient"),
    path("login/register_medic/", RegisterMedicView.as_view(), name="RegisterMedic")
]
