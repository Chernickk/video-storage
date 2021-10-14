from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from .models import Record
from .serializers import RecordSerializer


class RecordViewSet(ListModelMixin, GenericViewSet):
    queryset = Record.objects.filter(is_deleted=False)
    serializer_class = RecordSerializer

