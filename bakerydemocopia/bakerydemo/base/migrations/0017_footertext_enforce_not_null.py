# Generated by Django 4.2 on 2023-05-15 10:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0016_footertext_bootstrap_translation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footertext",
            name="locale",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailcore.locale",
            ),
        ),
        migrations.AlterField(
            model_name="footertext",
            name="translation_key",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterUniqueTogether(
            name="footertext",
            unique_together={("translation_key", "locale")},
        ),
    ]
