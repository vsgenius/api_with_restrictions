import django_filters
from django_filters import rest_framework as filters
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    creator = django_filters.CharFilter()
    created_at = django_filters.DateFromToRangeFilter()
    status = django_filters.CharFilter()
    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at','status']