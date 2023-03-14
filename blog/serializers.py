from rest_framework import serializers

from .models import Blog
from property_andalucia_api.validators import validate_image


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

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Blog()
        fields = [
            'id',
            'owner',
            'is_owner',
            'title',
            'content',
            'image',
            'created_on',
            'updated_at',
            'profile_id',
            'profile_image',
        ]
