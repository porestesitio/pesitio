# Generated by Django 3.0.7 on 2020-07-09 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0006_auto_20200708_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='imagen_articulo',
            field=models.ImageField(blank=True, help_text='Imagen del artículo', null=True, upload_to=''),
        ),
    ]
