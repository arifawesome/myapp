from rest_framework import serializers
from devices.models import Iphone, Macbook,Ipad,SamsungPhone,GooglePhone
    
class IphoneSerializer(serializers.ModelSerializer):
    class Meta:
            model = Iphone
            fields = '__all__'

class MacbookSerializer(serializers.ModelSerializer):
    class Meta:
            model = Macbook
            fields = '__all__'

class IpadSerializer(serializers.ModelSerializer):
    class Meta:
            model = Ipad
            fields = '__all__'

class SamsungPhoneSerializer(serializers.ModelSerializer):
    class Meta:
            model = SamsungPhone
            fields = '__all__'

class GooglePhoneSerializer(serializers.ModelSerializer):
    class Meta:
            model = GooglePhone
            fields = '__all__'