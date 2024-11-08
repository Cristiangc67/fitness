from django.urls import path
from .views import HomeView, AboutUsView, LogInView

urlpatterns = [
    path("", HomeView.as_view(), name="Home"),
    path("about/", AboutUsView.as_view(), name="About"),
    path("login/", LogInView.as_view(), name="Login"),
]
