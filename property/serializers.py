from rest_framework import serializers

from .models import Property
from property_andalucia_api.validators import validate_image
from saves.models import Save

""" Code adapted from Code Institute's "Django REST" walkthrough. """


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_email = serializers.ReadOnlyField(
        source='owner.profile.email'
    )
    profile_telephone = serializers.ReadOnlyField(
        source='owner.profile.telephone'
    )
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    save_id = serializers.SerializerMethodField()
    saves_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_save_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user,
                property=obj
            ).first()
            return save.id if save else None
        return None

    def validate_image(self, value):
        valid_image = validate_image(value)
        return valid_image

    class Meta:
        model = Property
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_email',
            'profile_telephone',
            'profile_image',
            'save_id',
            'saves_count',
            'name',
            'property_type',
            'province',
            'street',
            'municipality',
            'post_code',
            'price',
            'size',
            'bedroom_count',
            'bathrooms_count',
            'garage',
            'garden',
            'is_south_facing',
            'description',
            'image',
            'sold',
            'latitude',
            'longitude',
            'created_at',
            'updated_at',
        ]
