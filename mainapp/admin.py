from django.contrib import admin

from .models import Record, Car, GPS, Item


admin.site.register(Record)
admin.site.register(Car)
admin.site.register(GPS)
admin.site.register(Item)
