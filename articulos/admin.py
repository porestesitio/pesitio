from django.contrib import admin

# Register your models here.

from articulos.models import Familia, Medida, Articulos

admin.site.register(Familia)
admin.site.register(Medida)
admin.site.register(Articulos)