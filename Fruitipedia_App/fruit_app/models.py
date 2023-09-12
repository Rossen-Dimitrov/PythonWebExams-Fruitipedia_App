from django.core import validators
from django.db import models
from Fruitipedia_App.my_app_validators import validate_only_letters


class FruitModel(models.Model):
    MIN_LEN_NAME = 2
    MAX_LEN_NAME = 30

    name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            validators.MaxLengthValidator(MIN_LEN_NAME),
            validate_only_letters,
        ),
        null = False,
        blank = False,
    ),

    image_url = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    nutrition = models.TextField(
        null=True,
        blank=True,
    )

