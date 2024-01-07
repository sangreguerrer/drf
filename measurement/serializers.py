from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from measurement.models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']

    def validate(self, attrs):
        if attrs['sensor'].id == 1:
            raise ValidationError('The measurement error')
        return attrs


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)
    name = serializers.CharField(min_length=5)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

    def validate_name(self, value):
        if 'text' in value:
            raise ValidationError('The word "text" cannot be used')
        return value

    def validate(self, attrs):
        if 'hello' in attrs['name'] or id == 1:
            raise ValidationError('The sensor name error')
        return attrs

    def create(self,validated_data):
        print(f'Creating{validated_data}')
        return super().create(validated_data)
