from rest_framework import serializers
from .models import Save


class SaveSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Save
        fields = [
            'id',
            'owner',
            'property',
            'created_at',
        ]
