from django.urls import path

from registrar import views

urlpatterns = [
    path('', views.registrar, name="Registrar"),
]
