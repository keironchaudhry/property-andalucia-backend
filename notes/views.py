from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer
from property_andalucia_api.mixins import CustomQuerysetFilter
from property_andalucia_api.permissions import IsOwnerOrReadOnly


class NoteList(CustomQuerysetFilter, generics.ListCreateAPIView):
    """ Obtains and lists all note objects """
    model = Note
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetail(CustomQuerysetFilter, generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve or update a note when "owner" """
    model = Note
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = NoteSerializer
