from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from property_andalucia_api.permissions import IsOwnerOrReadOnly


class NoteList(generics.ListAPIView):
    """ Obtains and lists all note objects """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateAPIView):
    """ Retrieve or update a note when "owner" """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
