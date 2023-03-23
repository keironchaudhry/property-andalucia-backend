from django_filters import rest_framework as filters

from .models import Property

# The following links were useful as tutorials in
# the development and understanding of custom filters.
# URL: www.youtube.com/watch?v=s9V9F9Jtj7Q&t=248s
# URL: www.geeksforgeeks.org/customizing-filters-in-django-rest-framework/


class CustomFilters(filters.FilterSet):
    property_type = filters.ChoiceFilter(
        choices=Property.property_type_choices
    )
    province = filters.ChoiceFilter(
        choices=Property.province_choices
    )
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
            'property_type',
            'province',
            'price',
            'bedroom_count',
            'bathrooms_count',
            'garage',
            'garden',
            'is_south_facing',
            'sold',
        ]
