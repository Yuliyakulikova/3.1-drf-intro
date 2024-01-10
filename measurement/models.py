from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=128)


class Measurement(models.Model):
    temperature = models.FloatField()
    date_and_time = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey('Sensor', related_name='measurements', on_delete=models.CASCADE)