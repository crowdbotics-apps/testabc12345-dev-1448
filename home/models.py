from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    ttest = models.OneToOneField(
        "home.HomePage",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_ttest",
    )
    test = models.ManyToManyField(
        "users.User", blank=True, related_name="customtext_test",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Test(models.Model):
    "Generated Model"
    gfgfh = models.PositiveIntegerField()
    test = models.OneToOneField(
        "home.CustomText",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="test_test",
    )
    ttestt = models.OneToOneField(
        "home.HomePage",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="test_ttestt",
    )
    testhk = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="test_testhk",
    )
    tesst = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="test_tesst",
    )
