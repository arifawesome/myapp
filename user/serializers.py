from .models import UserInfo,UserTradeInfo
from rest_framework import serializers
from django.contrib.auth.models import User


class UserInfoSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = UserInfo
        fields = '__all__'

class UserTradeInfoSerializer(serializers.ModelSerializer):

    user=serializers.ReadOnlyField(source='user.username')
    address=serializers.ReadOnlyField(source='address.addressLine1')
    class Meta:
        model = UserTradeInfo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = User
        fields = ['id', 'username', 'email']