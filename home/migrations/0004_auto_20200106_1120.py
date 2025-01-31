# Generated by Django 2.2.9 on 2020-01-06 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0003_test_test"),
    ]

    operations = [
        migrations.AddField(
            model_name="test",
            name="one",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="test_one",
                to="home.HomePage",
            ),
        ),
        migrations.AddField(
            model_name="test",
            name="onetwo",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="test_onetwo",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="test",
            name="ttest",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="test_ttest",
                to="home.CustomText",
            ),
        ),
    ]
