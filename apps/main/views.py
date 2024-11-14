from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context["is_authenticated"] = self.request.user.is_authenticated
        return context


class AboutUsView(TemplateView):
    template_name = "main/about.html"


class LogInView(TemplateView):
    template_name = "main/login.html"
