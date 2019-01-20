from django.db import models


# Create your models here.


class sensorData(models.Model):
    nodeKey = models.TextField(null=True)
    flowData = models.TextField(null=True)
    paData = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
