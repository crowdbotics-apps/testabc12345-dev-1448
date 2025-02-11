# Generated by Django 2.2.9 on 2020-01-06 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0011_auto_20200106_1138"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="test",
            field=models.ManyToManyField(
                blank=True, related_name="customtext_test", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="customtext",
            name="ttest",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customtext_ttest",
                to="home.HomePage",
            ),
        ),
    ]
