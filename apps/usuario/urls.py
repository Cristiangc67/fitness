from django.urls import path
from .views import UserView, UserUpdateView, PacientsView, ClienteChatRedirectView, SugerirPlanView

urlpatterns = [
    path("<int:pk>/", UserView.as_view(), name="perfil"),
    path("<int:pk>/editar/", UserUpdateView.as_view(), name="editar_perfil"),
    path("<int:pk>/pacientes/", PacientsView.as_view(), name="medico-pacientes"),
    path("<int:pk>/chat/", ClienteChatRedirectView.as_view(), name="cliente-chat"),
    path('<int:cliente_pk>/sugerir-plan/', SugerirPlanView.as_view(), name='sugerir-plan'),
]
