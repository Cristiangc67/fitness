from django.urls import path
from .views import ChatTest

urlpatterns = [path("<int:conversation_id>/", ChatTest.as_view(), name="chatTest")]
