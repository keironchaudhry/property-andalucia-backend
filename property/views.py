from .models import Property
from .serializers import PropertySerializer


class PropertyList(ListAPIView):
    """ Obtains and lists all property objects """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
