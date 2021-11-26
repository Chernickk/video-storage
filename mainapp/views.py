import os
from datetime import datetime
from wsgiref.util import FileWrapper

from django.conf import settings
from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import HttpResponse

from .models import Car, Request
from .serializers import CarSerializer, RequestSerializer


def video_view(request, filename):
    file = FileWrapper(open(f'{os.path.join(settings.TEMP_MEDIA_FOLDER, filename)}', 'rb'))
    response = HttpResponse(file, content_type='video/mp4')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response


# class PostRequest(APIView):
#     def post(self, request):
#         try:
#             dt = datetime.strptime(self.request.data['datetime'], '%d.%m.%Y, %H:%M:%S')
#             license_table = self.request.data['car_id']
#             order = self.request.data['id']
#
#             records = find_clips(license_table, dt)
#             merge_clips(records, order)
#
#             return JsonResponse({
#                 'status': 'OK'
#             })
#         except Exception:
#             return JsonResponse({
#                 'status': 'FAIL'
#             })


class CarViewSet(mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class RequestViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
