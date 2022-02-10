from django_filters import rest_framework as filters

from ..models import Event


class EventFilter(filters.FilterSet):
    date = filters.DateRangeFilter(
        label='Период времени',
    )

    class Meta:
        model = Event
        fields = (
            'date',
        )
