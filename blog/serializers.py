from rest_framework import serializers

from .models import Blog
from property_andalucia_api.validators import (
    validate_image,
    validate_empty_field
)

""" Code adapted from Code Institute's "Django REST" walkthrough. """


class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        valid_image = validate_image(value)
        return valid_image

    def validate_title(self, value):
        valid_title = validate_empty_field(value)
        return valid_title

    def validate_content(self, value):
        valid_content = validate_empty_field(value)
        return valid_content

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Blog
        fields = [
            'id',
            'owner',
            'is_owner',
            'title',
            'content',
            'image',
            'created_at',
            'updated_at',
            'profile_id',
            'profile_image',
        ]
