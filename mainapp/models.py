from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'car'


class Record(models.Model):
    file_name = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'record'
