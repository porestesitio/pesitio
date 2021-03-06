# Generated by Django 3.0.7 on 2020-07-08 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0003_auto_20200708_0257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, help_text='Nombre del artículo', max_length=30, null=True)),
                ('descrip_corta', models.CharField(blank=True, help_text='Pequeña descripción', max_length=40, null=True)),
                ('Descrip_larga', models.CharField(blank=True, help_text='Descripción', max_length=100, null=True)),
                ('estado_articulo', models.CharField(choices=[('0', 'Por autorizar'), ('a', 'Autorizado'), ('b', 'baja')], default='0', help_text='Situación del artículo', max_length=1)),
                ('precio_articulo', models.DecimalField(decimal_places=2, default='0.00', help_text='Precio unitario', max_digits=8)),
                ('precio_envio', models.DecimalField(decimal_places=2, default='0.00', help_text='Precio envío', max_digits=6)),
                ('precio_mayoreo', models.DecimalField(decimal_places=2, default='0.00', help_text='Precio mayoreo', max_digits=8)),
                ('tipo_descuento', models.CharField(choices=[('s', 'Sin descuento'), ('p', 'Porcentaje'), ('v', 'Valor')], default='s', help_text='Tipos de descuento', max_length=1)),
                ('descuento', models.DecimalField(decimal_places=2, default='0.00', help_text='Descuento ', max_digits=8)),
                ('imagen_articulo', models.ImageField(help_text='Imagen del artículo', upload_to='')),
                ('nota_rechazo', models.CharField(help_text='Nota de rechazo de publicación', max_length=200)),
                ('fecha_empieza_publicacion', models.DateTimeField(null=True)),
                ('fecha_caducidad', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Alta del artículo')),
                ('updated', models.DateTimeField(auto_now_add=True, help_text='Ultima modificación del artículo')),
            ],
            options={
                'verbose_name': 'articulo',
                'verbose_name_plural': 'articulos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familia', models.CharField(blank=True, max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['familia'],
            },
        ),
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medida', models.CharField(blank=True, max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['medida'],
            },
        ),
        migrations.DeleteModel(
            name='Articulos1',
        ),
        migrations.DeleteModel(
            name='Familia1',
        ),
        migrations.DeleteModel(
            name='Medida1',
        ),
        migrations.AddField(
            model_name='articulos',
            name='familia',
            field=models.ForeignKey(blank=True, help_text='Familia', on_delete=django.db.models.deletion.CASCADE, to='articulos.Familia'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='medida',
            field=models.ForeignKey(help_text='Unidad de medida', on_delete=django.db.models.deletion.CASCADE, to='articulos.Medida'),
        ),
    ]
