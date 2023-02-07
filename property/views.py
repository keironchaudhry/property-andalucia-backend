from django.db.models import Count
from rest_framework import generics, filters

from property_andalucia_api.permissions import IsOwnerOrReadOnly, IsSeller
from .serializers import PropertySerializer
from .models import Property


class PropertyList(generics.ListAPIView):
    """ Obtains and lists all property objects """
    filter_backends = [filters.OrderingFilter]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyCreate(generics.CreateAPIView):
    """ Allows users that are Sellers-only to access property creation """
    serializer_class = PropertySerializer
    permission_classes = [IsSeller]
    queryset = Property.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or destroy a single property object when "owner" """
    queryset = Property.objects.annotate(
        saves_count=Count('saves', distinct=True),
    ).order_by('-created_at')
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PropertySerializer
