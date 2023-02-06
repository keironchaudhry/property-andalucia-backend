from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer
from property_andalucia_api.permissions import IsOwnerOrReadOnly


class NoteList(generics.ListCreateAPIView):
    """ Obtains and lists all note objects """
    model = Note
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# https://www.django-rest-framework.org/api-guide/filtering/
    def get_queryset(self):
        """ Reveals object queryset based on whether the defined user
        is the owner of the object or is anonymous """
        user = self.request.user
        if user.is_authenticated:
            queryset = self.model.objects.filter(
                owner=user
            )
        else:
            queryset = self.model.objects.none()
        return queryset


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve or update a note when "owner" """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
