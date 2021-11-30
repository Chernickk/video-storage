import os
from wsgiref.util import FileWrapper

from django.conf import settings
from rest_framework import mixins, viewsets
from django.shortcuts import HttpResponse

from .models import Car, Request
from .serializers import CarSerializer, RequestSerializer


def video_view(request, car_license_table, filename):
    print(os.path.join(settings.REQUEST_MEDIA_FOLDER, car_license_table, filename))
    file = FileWrapper(open(f'{os.path.join(settings.MEDIA_FOLDER, car_license_table, filename)}', 'rb'))
    response = HttpResponse(file, content_type='video/mp4')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response


class CarViewSet(mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class RequestViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
