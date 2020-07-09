from django.db import models

# Create your models here.

class Familia(models.Model):
    familia = models.CharField(max_length=30,null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["familia"]

    def __str__(self):
        return self.familia

class Medida(models.Model):
    medida = models.CharField(max_length=30,null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["medida"]

    def __str__(self):
        return self.medida


class Articulos(models.Model):
    nombre = models.CharField(max_length=30,null=True, blank=True, help_text='Nombre del artículo')
    familia = models.ForeignKey(Familia,
                                on_delete=models.CASCADE,
                                null=False,
                                blank=True, help_text='Familia') 
    medida = models.ForeignKey(Medida,
                                on_delete=models.CASCADE,
                                null=False,
                                blank=False, help_text='Unidad de medida') 
    descrip_corta = models.CharField(max_length=40,null=True, blank=True, help_text='Pequeña descripción')
    descrip_larga = models.CharField(max_length=100,null=True, blank=True, help_text='Descripción')
    estados_articulo = (
        ('0', 'Por autorizar'),
        ('a', 'Autorizado'),
        ('b', 'baja'),
    )
    estado_articulo = models.CharField(max_length=1, choices=estados_articulo, default='0', help_text='Situación del artículo')
    precio_articulo = models.DecimalField(max_digits=8, decimal_places=2, default='0.00', help_text='Precio unitario')
    precio_envio = models.DecimalField(max_digits=6, decimal_places=2, default='0.00', help_text='Precio envío')
    precio_mayoreo = models.DecimalField(max_digits=8, decimal_places=2, default='0.00', help_text='Precio mayoreo')
    tipos_descuento = (
        ('s', 'Sin descuento'),
        ('p', 'Porcentaje'),
        ('v', 'Valor'),
    )
    tipo_descuento = models.CharField(max_length=1, choices=tipos_descuento, default='s', help_text='Tipos de descuento')
    descuento = models.DecimalField(max_digits=8, decimal_places=2, default='0.00', help_text='Descuento ')
    imagen_articulo = models.ImageField(help_text='Imagen del artículo', null=True, blank=True)
    nota_rechazo = models.CharField(max_length=200, help_text='Nota de rechazo de publicación')
    fecha_empieza_publicacion = models.DateTimeField(null=True)
    fecha_caducidad = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True, help_text='Alta del artículo')
    updated = models.DateTimeField(auto_now_add=True, help_text='Ultima modificación del artículo')

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'articulo'
        verbose_name_plural = 'articulos'

    def __str__(self):
        return self.nombre

