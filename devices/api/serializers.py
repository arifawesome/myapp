from rest_framework import serializers
from devices.models import Iphone, Macbook
    
class IphoneSerializer(serializers.ModelSerializer):
    class Meta:
            model = Iphone
            fields = '__all__'

class MacbookSerializer(serializers.ModelSerializer):
    class Meta:
            model = Macbook
            fields = '__all__'