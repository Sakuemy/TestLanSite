from django.shortcuts import render

from .models import PointData, CheckLog

def index(request):
    list_PointData = PointData.objects.order_by('id')
    return render(request, 'testlanapp/list.html', {'list_PointData': list_PointData})