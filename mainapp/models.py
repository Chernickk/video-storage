import os

from django.db import models
from django.conf import settings


class Car(models.Model):
    name = models.CharField(max_length=255)
    license_table = models.CharField(max_length=15, null=True)
    ip_address = models.CharField(max_length=16, null=True)
    last_seen = models.DateTimeField(null=True)
    online = models.BooleanField(default=False)

    class Meta:
        db_table = 'car'


class Action(models.Model):
    uuid = models.CharField(max_length=128)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    class Meta:
        db_table = 'action'


class Request(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    delivered = models.BooleanField(default=False)
    record_status = models.BooleanField(null=True)

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

    def delete(self, using=None, keep_parents=False):
        if not self.request:
            path = os.path.join(settings.REQUEST_MEDIA_FOLDER, self.car.license_table, 'temp', self.file_name)
        else:
            path = os.path.join(settings.REQUEST_MEDIA_FOLDER, self.car.license_table, 'requests', self.file_name)

        if os.path.exists(path):
            os.remove(path)

        return super().delete()


class GPS(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'gps'
