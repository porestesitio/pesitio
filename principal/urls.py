from django.urls import path

from principal import views

urlpatterns = [
    path('', views.principal, name="Principal"),
]
