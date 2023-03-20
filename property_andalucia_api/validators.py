import re

from rest_framework import serializers
from django.core.validators import RegexValidator

validate_numbers = RegexValidator(
    (
        '^\\d+$'
    )
)


def validate_telephone_number(value):
    # https://www.sololearn.com/discuss/2588446/solved-python-phone-number-validator
    # Above link aided me in the creation of this particular function.
    # Allows only 9 numeric digits as a Spanish telephone number.
    regex = re.compile(
        r'^[697][0-9]{8}$'
    )
    if re.fullmatch(regex, value):
        return value
    raise serializers.ValidationError(
        'Enter a valid Spanish number (9-digits, starting with 6, 7 or 9).'
    )


def validate_image(value):
    # Credit owed to CI Django REST Framework project for code basis.
    # https://github.com/Code-Institute-Solutions/drf-api
    max_height = 4096
    max_width = 4096
    maximum_file_size = 2

    if value.size > (1024 * 1024 * maximum_file_size):
        raise serializers.ValidationError(
            'Image size must be smaller than 2MB.'
        )
    if value.image.height > max_height:
        raise serializers.ValidationError(
            'Image height must be smaller than 4096px.'
        )
    if value.image.width > max_width:
        raise serializers.ValidationError(
            'Image width must be smaller than 4096px.'
        )
    return value


def validate_email_address(value):
    # https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/
    # Credit: The above link helped me understand
    # how to create the logic for this function
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    )
    if re.fullmatch(regex, value):
        return value
    raise serializers.ValidationError(
        'Please enter a valid email address.'
    )


def validate_empty_field(value):
    if value == '':
        raise serializers.ValidationError(
            'This field cannot be left empty.'
        )
    return value
