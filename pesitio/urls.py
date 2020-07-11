"""pesitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import registro_usuario

urlpatterns = [
    path('padmin', admin.site.urls),
    path('parts/', include('articulos.urls')),
    path('pblog/', include('blog.urls')),
    path('pcontacto/', include('contacto.urls')),
    path('pempleos/', include('empleos.urls')),
    path('pentrada/', include('entrada.urls')),
    path('', include('principal.urls')),
    path('pservicios/', include('servicios.urls')),
    path('pcuenta/',include('django.contrib.auth.urls')),
    path('pregistro',registro_usuario, name='registro_usuario'), 
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)