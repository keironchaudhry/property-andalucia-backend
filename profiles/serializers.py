from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    seller_status = serializers.ReadOnlyField(source="owner.seller_status")

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'is_owner',
            'seller_status',
            'name',
            'bio',
            'email',
            'telephone',
            'image',
            'created_at',
            'updated_at'
        ]
