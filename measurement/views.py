# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from measurement.models import Measurement, Sensor
from measurement.serializers import SensorDetailSerializer,MeasurementSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'description', ]
    search_fields = ['name', 'description', ]
    ordering_fields = ['id', 'name', 'description', 'measurements']
    pagination_class = LimitOffsetPagination


class MeasureViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['sensor', 'created_at', ]
    search_fields = ['sensor', 'created_at', ]
    ordering_fields = ['sensor', ]





