from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = "main/home.html"


class AboutUsView(TemplateView):
    template_name = "main/about.html"


class LogInView(TemplateView):
    template_name = "main/login.html"
