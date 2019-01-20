from django.shortcuts import render
from .models import sensorData
from django.http import HttpResponse
# Create your views here.


class sensorCrud():

    def uploadData(request):
        insertSensorData = sensorData.objects.create()
        insertSensorData.nodeKey = request.GET['nodeKey']
        insertSensorData.flowData = request.GET['flowData']
        insertSensorData.paData = request.GET['paData']


        if(insertSensorData.save()):
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=503)
