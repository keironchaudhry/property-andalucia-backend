from rest_framework import generics, permissions
from property_andalucia_api.mixins import CustomQuerysetFilter
from property_andalucia_api.permissions import IsOwnerOrReadOnly
from .serializers import SaveSerializer
from .models import Save

""" Code adapted from Code Institute's "Django REST" walkthrough. """


class SaveList(CustomQuerysetFilter, generics.ListCreateAPIView):
    """ Obtains and lists all save objects """
    model = Save
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SaveDetail(CustomQuerysetFilter, generics.RetrieveDestroyAPIView):
    """ Obtains a detail view of a save object if "owner" """
    model = Save
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SaveSerializer
