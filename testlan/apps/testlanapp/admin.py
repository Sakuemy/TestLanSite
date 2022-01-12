from django.contrib import admin

from .models import PointData, Alert

admin.site.register(PointData)
admin.site.register(Alert)