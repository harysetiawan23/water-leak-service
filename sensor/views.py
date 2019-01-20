from django.shortcuts import render
from .models import sensorData
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


class sensorCrud():


    @api_view(['GET'])
    def uploadData(request):

        if request.method == 'GET':
            insertSensorData = sensorData.objects.create()
            insertSensorData.nodeKey = request.GET['nodeKey']
            insertSensorData.flowData = request.GET['flowData']
            insertSensorData.paData = request.GET['paData']


            if(insertSensorData.save()):
                return HttpResponse(status=status.HTTP_200_OK)
            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
