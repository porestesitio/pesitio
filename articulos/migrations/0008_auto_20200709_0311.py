# Generated by Django 3.0.7 on 2020-07-09 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0007_auto_20200709_0102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulos',
            old_name='Descrip_larga',
            new_name='descrip_larga',
        ),
    ]
