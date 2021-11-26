from django.contrib import admin

from .models import Record, Car, Action, Request


admin.site.register(Record)
admin.site.register(Car)
admin.site.register(Request)
admin.site.register(Action)
