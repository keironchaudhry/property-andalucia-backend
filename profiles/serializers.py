from rest_framework import serializers

from .models import Profile
from property_andalucia_api.validators import (
    validate_image,
    validate_email_address,
    validate_telephone_number,
)
from followers.models import Follower

""" Code adapted from Code Institute's "Django REST" walkthrough. """


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

    def validate_image(self, value):
        valid_image = validate_image(value)
        return valid_image

    def validate_email(self, value):
        valid_email = validate_email_address(value)
        return valid_email

    def validate_telephone(self, value):
        valid_telephone_number = validate_telephone_number(value)
        return valid_telephone_number

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
