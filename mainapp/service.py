import os
from datetime import datetime

from django.conf import settings
from django.db.models import Q

from .models import Record, Car


def find_clips(license_table: str, start_dt: datetime, finish_dt: datetime):
    car = Car.objects.get(pk=license_table)

    q = (Q(start_time__gte=start_dt, start_time__lte=finish_dt) |
         Q(end_time__gte=start_dt, end_time__lte=finish_dt)) & Q(car=car)

    records = Record.objects.filter(q)

    records_with_path = [os.path.join(settings.MEDIA_PATH, record.file_name) for record in records]

    return records_with_path


