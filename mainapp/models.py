from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'car'


class Action(models.Model):
    uuid = models.CharField(max_length=128)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    class Meta:
        db_table = 'action'


class Record(models.Model):
    item = models.ForeignKey(Action,
                             on_delete=models.PROTECT,
                             null=True)
    file_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    car = models.ForeignKey(Car, on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'record'


class GPS(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'gps'
