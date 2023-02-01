from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer
from property_andalucia_api.permissions import IsOwnerOrReadOnly


class NoteList(generics.ListCreateAPIView):
    """ Obtains and lists all note objects """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve or update a note when "owner" """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
