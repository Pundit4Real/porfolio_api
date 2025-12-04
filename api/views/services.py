from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from api.models.services import Service
from api.serializers.services import ServiceSerializer
from api.utils.hero_mixin import HeroPageMixin


# -----------------------------
# Custom Filter
# -----------------------------
class ServiceFilter(filters.FilterSet):
    category_name = filters.CharFilter(field_name="categories__name", lookup_expr='iexact')
    category_name_icontains = filters.CharFilter(field_name="categories__name", lookup_expr='icontains')

    class Meta:
        model = Service
        fields = ['highlight', 'is_active', 'categories', 'category_name', 'category_name_icontains']


class ServiceViewSet(HeroPageMixin, viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServiceFilter
    hero_page = "services"
