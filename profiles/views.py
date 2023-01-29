from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from property_andalucia_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """ Obtains and lists all profile objects """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """ Retrieve or update a profile when "owner" """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
