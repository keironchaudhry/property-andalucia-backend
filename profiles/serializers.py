from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    seller_status = serializers.ReadOnlyField(source='owner.seller_status')
    following_id = serializers.SerializerMethodField()
    propertys_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user,
                followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'is_owner',
            'seller_status',
            'following_id',
            'propertys_count',
            'followers_count',
            'following_count',
            'name',
            'bio',
            'email',
            'telephone',
            'image',
            'created_at',
            'updated_at'
        ]
