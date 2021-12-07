import os

from django.db import models
from django.conf import settings


class Car(models.Model):
    name = models.CharField(max_length=255)
    license_table = models.CharField(max_length=15, null=True)
    ip_address = models.CharField(max_length=16, null=True)
    last_seen = models.DateTimeField(null=True)
    online = models.BooleanField(default=False)
    loading = models.BooleanField(default=False)

    class Meta:
        db_table = 'car'


class Action(models.Model):
    uuid = models.CharField(max_length=128)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    class Meta:
        db_table = 'action'


class Request(models.Model):
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    delivered = models.BooleanField(default=False)
    record_status = models.BooleanField(null=True)

    def delete(self, *args, **kwargs):
        records = Record.objects.filter(request__pk=self.pk)
        for record in records:
            record.delete()

        return super().delete(*args, **kwargs)

    class Meta:
        db_table = 'request'


class Record(models.Model):
    action = models.ForeignKey(Action,
                               on_delete=models.PROTECT,
                               null=True)
    file_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    car = models.ForeignKey(Car, on_delete=models.PROTECT, null=True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, null=True, related_name='records')

    class Meta:
        db_table = 'record'

    def delete(self, *args, **kwargs):
        if not self.request:
            path = os.path.join(settings.MEDIA_FOLDER, self.car.license_table, 'temp', self.file_name)
        else:
            path = os.path.join(settings.MEDIA_FOLDER, self.car.license_table, 'requests', self.file_name)

        if os.path.exists(path):
            os.remove(path)

        return super().delete(*args, **kwargs)


class GPS(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'gps'
