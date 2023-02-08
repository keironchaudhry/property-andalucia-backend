from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Note
from .serializers import NoteSerializer
from property_andalucia_api.mixins import CustomQuerysetFilter
from property_andalucia_api.permissions import IsOwnerOrReadOnly


class NoteList(CustomQuerysetFilter, generics.ListCreateAPIView):
    """ Obtains and lists all note objects """
    model = Note
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['property']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetail(CustomQuerysetFilter, generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve or update a note when "owner" """
    model = Note
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = NoteSerializer
