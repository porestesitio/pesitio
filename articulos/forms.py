from django import forms
from django.forms import ModelForm
from .models import Articulos

class ArticuloForm(ModelForm):

    class Meta:
        model = Articulos
        fields = ['nombre',
                'familia',
                'medida',
                'descrip_corta',
                'descrip_larga',
                'estado_articulo',
                'precio_articulo',
                'precio_envio',
                'precio_mayoreo',
                'tipo_descuento',
                'descuento',
                'imagen_articulo',
                'nota_rechazo',
                'fecha_empieza_publicacion',
                'fecha_caducidad',]