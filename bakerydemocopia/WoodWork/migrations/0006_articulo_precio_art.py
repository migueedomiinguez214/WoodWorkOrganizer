# Generated by Django 4.2.7 on 2023-11-21 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WoodWork', '0005_articulo_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='Precio_art',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]