# Generated by Django 4.2.7 on 2023-11-21 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WoodWork', '0007_rename_precio_art_articulo_precio_art'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='precio_art',
        ),
    ]
