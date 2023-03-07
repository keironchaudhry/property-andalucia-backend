from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Note

""" Code adapted from Code Institute's "Django REST" walkthrough. """


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Note
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'property',
            'content',
            'created_at',
            'updated_at'
        ]


class NoteDetailSerializer(NoteSerializer):

    property = serializers.ReadOnlyField(
        source='property.id'
    )
