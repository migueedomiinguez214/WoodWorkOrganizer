# Generated by Django 4.2.7 on 2023-11-20 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WoodWork', '0002_remove_presupuesto_fecha_entrega_presupuesto_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='correo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
