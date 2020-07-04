from django.urls import path

from registrar.views import RegistroUsuario

urlpatterns = [
    path('', RegistroUsuario.as_view(), name="Registrar"),
]
