from rest_framework import generics, permissions
from property_andalucia_api.permissions import IsOwnerOrReadOnly
from .serializers import FollowerSerializer
from .models import Follower

""" Code adapted from Code Institute's "Django REST" walkthrough. """


class FollowerList(generics.ListCreateAPIView):
    """ Obtains and lists all follow objects """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """ Retrieve or destroy a single follow object when "owner" """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
