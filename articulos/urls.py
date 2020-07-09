from django.urls import path

from articulos import views


urlpatterns = [
    path('', views.varticulos, name="Arts"),
]
