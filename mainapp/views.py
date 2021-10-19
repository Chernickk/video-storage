from datetime import datetime
from wsgiref.util import FileWrapper

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse

from .service import get_output_file
from .models import Car
from .serializers import CarSerializer


def index(request):
    return render(request, 'index.html')


def video_view(request, filename):
    file = FileWrapper(open(f'{filename}', 'rb'))
    response = HttpResponse(file, content_type='video/avi')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response


class GetRecordLink(APIView):
    def get(self, request):

        car_id = request.query_params.get('car_id')

        if not car_id:
            return Response({
                'status': 'Please select car'
            })

        from_time = datetime.strptime(request.query_params.get('from_time'), '%d.%m.%Y, %H:%M:%S')
        to_time = datetime.strptime(request.query_params.get('to_time'), '%d.%m.%Y, %H:%M:%S')
        output_file = get_output_file(start_time=from_time, end_time=to_time, car_id=car_id)

        if output_file:
            link = {
                'status': 'OK',
                'filename': output_file
            }
        else:
            link = {
                'status': 'file not found'
            }

        return Response(link)


class GetCars(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()