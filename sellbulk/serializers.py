from rest_framework import serializers
from .models import Devices,Inquerer
class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'

class InquererSerializer(serializers.ModelSerializer):
    devices = DevicesSerializer(many=True)

    class Meta:
        model = Inquerer
        fields = ['email', 'firstName', 'lastName','devices']

    def create(self, validated_data):
        devices_data = validated_data.pop('devices')
        inquerer = Inquerer.objects.create(**validated_data)
        for device_data in devices_data:
            Devices.objects.create(inquerer=inquerer, **device_data)
        return inquerer
