from rest_framework import serializers

# Credit owed to Code Institute Django REST Framework project for code basis.
# https://github.com/Code-Institute-Solutions/drf-api


def validate_image(value):
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
