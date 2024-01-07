from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor}:{self.created_at}'