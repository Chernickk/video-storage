from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from mainapp.views import CarViewSet, RequestViewSet

router = DefaultRouter(trailing_slash=False)
router.register('cars', CarViewSet, basename='cars')
router.register('requests', RequestViewSet, basename='requests')


urlpatterns = [
    # path('media/<str:filename>', video_view),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name='index.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
