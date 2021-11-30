from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255)
    license_table = models.CharField(max_length=15, null=True)

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


class GPS(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'gps'
