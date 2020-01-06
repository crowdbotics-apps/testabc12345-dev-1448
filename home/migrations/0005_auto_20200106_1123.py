# Generated by Django 2.2.9 on 2020-01-06 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0004_auto_20200106_1120"),
    ]

    operations = [
        migrations.RemoveField(model_name="test", name="onetwo",),
        migrations.AddField(
            model_name="test",
            name="many",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="test_many",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
