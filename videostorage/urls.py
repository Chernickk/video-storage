from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mainapp.views import RecordViewSet

router = DefaultRouter()
router.register('records', RecordViewSet, basename='records')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
