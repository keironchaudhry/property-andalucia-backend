from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


""" Code adapted from Code Institute's "Django REST" walkthrough. """


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id',
            'profile_image',
            'seller_status',
            'is_staff',
        )
