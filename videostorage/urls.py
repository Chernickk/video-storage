from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from mainapp.views import GetRecordLink, GetCars, index, video_view


urlpatterns = [
    path('media/<str:filename>', video_view),
    path('admin/', admin.site.urls),
    path('api/get_record_link', GetRecordLink.as_view()),
    path('api/get_cars', GetCars.as_view({'get': 'list'})),
    re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name='index.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
