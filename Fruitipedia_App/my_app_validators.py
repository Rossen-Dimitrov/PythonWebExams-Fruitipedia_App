from django.core import exceptions


def validate_only_letters(value):
    for char in value:
        if not char.isalnum():
            raise exceptions.ValidationError("Fruit name should contain only letters!")


def validate_starts_with_letter(value):
    if not value[0].isalnum():
        raise exceptions.ValidationError("Your name must start with a letter!")
