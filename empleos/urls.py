from django.urls import path

from empleos import views


urlpatterns = [
    path('', views.empleos, name="Empleos"),
]
