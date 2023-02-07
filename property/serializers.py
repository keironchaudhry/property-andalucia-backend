from rest_framework import serializers
from .models import Property
from saves.models import Save


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
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

    class Meta:
        model = Property
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
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
