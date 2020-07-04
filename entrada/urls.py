from django.urls import path

from entrada import views


urlpatterns = [
    path('', views.entrada, name="Entrada"),
]
