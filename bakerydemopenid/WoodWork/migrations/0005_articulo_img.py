# Generated by Django 4.2.7 on 2023-11-20 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WoodWork', '0004_cliente_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='foto'),
        ),
    ]
