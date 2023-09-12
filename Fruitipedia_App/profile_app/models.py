from django.db import models
from django.core import validators
from Fruitipedia_App.my_app_validators import validate_starts_with_letter


class ProfileModel(models.Model):
    MIN_LEN_F_NAME = 2
    MAX_LEN_F_NAME = 25

    MIN_LEN_L_NAME = 1
    MAX_LEN_L_NAME = 35

    EMAIL_MAX_LEN = 40

    MIN_PASS_LEN = 8
    MAX_PASS_LEN = 20

    first_name = models.CharField(
        max_length=MAX_LEN_F_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_F_NAME),
            validate_starts_with_letter,
        ),
        null=False,
        blank=False
    )
    last_name = models.CharField(
        max_length=MAX_LEN_L_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_L_NAME),
            validate_starts_with_letter,
        ),
        null=False,
        blank=False
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LEN,
        null=False,
        blank=True,
    )

    password = models.CharField(
        max_length=MAX_PASS_LEN,
        validators=(
            validators.MinLengthValidator(MIN_PASS_LEN),
        ),
        null=False,
        blank=False
    )
