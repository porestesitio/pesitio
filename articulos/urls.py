from django.urls import path

from articulos import views


urlpatterns = [
    path('', views.varticulos, name="Arts"),
    path('articulo_nuevo/', views.vnuevo, name="ArtNuevo"),
    path('articulo_edita/', views.vnuevo, name="ArtEdita"),
    
]
