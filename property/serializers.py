from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    longitude = serializers.ReadOnlyField()
    latitude = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Property
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
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
