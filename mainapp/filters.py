from django_filters import DateTimeFilter
from django_filters.rest_framework import FilterSet

from .models import GPS


class GPSFilterSet(FilterSet):
    from_datetime = DateTimeFilter(field_name='datetime', lookup_expr='gte')
    to_datetime = DateTimeFilter(field_name='datetime', lookup_expr='lte')

    class Meta:
        model = GPS
        fields = ['from_datetime', 'to_datetime', 'car__id']
