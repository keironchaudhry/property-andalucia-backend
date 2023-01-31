from .models import Property
from .serializers import PropertySerializer
from rest_framework import generics


class PropertyList(generics.ListAPIView):
    """ Obtains and lists all property objects """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
