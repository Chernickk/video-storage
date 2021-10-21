from rest_framework import serializers

from .models import Record, Car, GPS


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class GPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPS
        fields = '__all__'
