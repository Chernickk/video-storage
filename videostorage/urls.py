from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from mainapp.views import GetRecordLink, GetCars, index, video_view


urlpatterns = [
    path('media/<str:filename>', video_view),
    path('admin/', admin.site.urls),
    path('api/get_record_link', GetRecordLink.as_view()),
    path('api/get_cars', GetCars.as_view({'get': 'list'})),
    re_path(r'^(?:.*)/?$', index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
