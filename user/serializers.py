from .models import UserInfo,UserTradeInfo,UserAddress
from rest_framework import serializers
from django.contrib.auth.models import User



class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserAddress
        fields=['addressType','addressLine1','addressLine2','city','state','zipcode','primaryAddress']

class UserInfoSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    useraddress=UserAddressSerializer(many=True)

    class Meta:
        model = UserInfo
        fields = ['user','useraddress','secondary_email','phoneNumber']

    def create(self, validated_data):
        addresses_data = validated_data.pop('useraddress')
        userinfo = UserInfo.objects.create(**validated_data)
        for address_data in addresses_data:
            UserAddress.objects.create(userinfo=userinfo, **address_data)
        return userinfo

    def update(self, instance, validated_data):
        addresses_data = validated_data.pop('useraddress')
        address = (instance.useraddress).all()
        address = list(address)
        instance.secondary_email = validated_data.get('econdary_email', instance.secondary_email)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.save()

        for addresses_data in addresses_data:
            address = address.pop(0)
            address.addressType = addresses_data.get('addressType', address.addressType)
            address.addressLine1 = addresses_data.get('addressLine1', address.addressLine1)
            address.addressLine2 = addresses_data.get('addressLine2', address.addressLine2)
            address.city = addresses_data.get('city', address.city)
            address.state = addresses_data.get('state', address.state)
            address.zipcode = addresses_data.get('zipcode', address.zipcode)
            address.primaryAddress = addresses_data.get('primaryAddress', address.primaryAddress)
            address.save()
        return instance

class UserTradeInfoSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    address=serializers.ReadOnlyField(source='address.addressLine1')
    
    class Meta:
        model = UserTradeInfo
        fields = ['user','tradeReferenceNo','status','address','orderDate','lableSent','shippingLableReceived','deviceReceived','deviceReview','deviceAccepted','paymentMethod','deviceShippingMethod','deviceTrackingInbound','deviceTrackingOutbound']

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']