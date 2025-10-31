from django.urls import path
from .views import LoginView, UsuarioView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("usuarios/", UsuarioView.as_view(), name="crear_usuario"),
    path("usuarios/<int:usuario_id>/", UsuarioView.as_view(), name="mod_usuario"),
]
