from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from property_andalucia_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """ Obtains and lists all profile objects """
    queryset = Profile.objects.annotate(
        propertys_count=Count('owner__property', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'propertys_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """ Retrieve or update a profile when "owner" """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        propertys_count=Count('owner__property', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
