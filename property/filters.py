from django_filters import rest_framework as filters

from .models import Property


class CustomFilters(filters.FilterSet):
    price = filters.RangeFilter(
        field_name='price'
    )
    bedroom_count = filters.NumberFilter(
        field_name='bedroom_count'
    )
    bathrooms_count = filters.NumberFilter(
        field_name='bathrooms_count'
    )
    garage = filters.BooleanFilter(
        field_name='garage'
    )
    garden = filters.BooleanFilter(
        field_name='garden'
    )
    is_south_facing = filters.BooleanFilter(
        field_name='is_south_facing'
    )
    sold = filters.BooleanFilter(
        field_name='sold'
    )

    class Meta:
        model = Property
        fields = [
            'owner__followed__owner__profile',
            'saves__owner__profile',
            'owner__profile',
            'price',
            'bedroom_count',
            'bathrooms_count',
            'garage',
            'garden',
            'is_south_facing',
            'sold',
        ]
