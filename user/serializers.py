from .models import UserInfo,UserTradeInfo,UserAddress,UserOrder
from rest_framework import serializers
from django.contrib.auth.models import User



class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserAddress
        fields=['addressType','addressLine1','addressLine2','city','state','zipcode','primaryAddress']

class UserInfoSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    useraddress=UserAddressSerializer(many=True)
    secondary_email=serializers.EmailField(max_length=None, min_length=None, allow_blank=True)
    phoneNumber=serializers.CharField(max_length=20, min_length=None, allow_blank=True, trim_whitespace=True)
    class Meta:
        model = UserInfo
        fields = ['user_id','user','useraddress','secondary_email','phoneNumber']

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
        instance.secondary_email = validated_data.get('secondary_email', instance.secondary_email)
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
    userorder=serializers.ReadOnlyField(source='userorder.user.username')
    address=serializers.ReadOnlyField(source='address.addressLine1')
    
    class Meta:
        model = UserTradeInfo
        fields = ['userorder','tradeReferenceNo','status','address','orderDate','lableSent','shippingLableReceived','deviceReceived','deviceReview','deviceAccepted','paymentMethod','deviceShippingMethod','deviceTrackingInbound','deviceTrackingOutbound']

class UserOrderSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    usertrade=UserTradeInfoSerializer(many=True)

    class Meta:
        model = UserOrder
        fields = ['user','usertrade',]

    def create(self, validated_data):
        orders_data = validated_data.pop('usertrade')
        userorder= UserOrder.objects.create(**validated_data)
        for order_data in orders_data:
            UserTradeInfo.objects.create(userorder=userorder, **order_data)
        return userorder

    def update(self, instance, validated_data):
        orders_data = validated_data.pop('usertrade')
        order = (instance.usertrade).all()
        order = list(order)
        instance.save()

        for orders_data in orders_data:
            order = order.pop(0)
            order.tradeReferenceNo = orders_data.get('tradeReferenceNo', order.tradeReferenceNo)
            order.status = orders_data.get('status', order.status)
            order.orderDate = orders_data.get('orderDate', order.orderDate)
            order.lableSent = orders_data.gett('lableSent', order.lableSent)
            order.shippingLableReceived = orders_data.get('shippingLableReceived', order.shippingLableReceived)
            order.deviceReceived = orders_data.get('deviceReceived', order.deviceReceived)
            order.deviceReview = orders_data.get('deviceReview', order.deviceReview)
            order.deviceAccepted = orders_data.get('deviceAccepted', order.deviceAccepted)
            order.deviceAcceptanceComment = orders_data.get('deviceAcceptanceComment', order.deviceAcceptanceComment)
            order.paymentMethod = orders_data.get('paymentMethod', order.paymentMethod)
            order.paymentReferenceNo = orders_data.gett('paymentReferenceNo', order.paymentReferenceNo)
            order.deviceShippingMethod = orders_data.get('deviceShippingMethod', order.deviceShippingMethod)
            order.deviceTrackingInbound = orders_data.get('deviceTrackingInbound', order.deviceTrackingInbound)
            order.deviceTrackingOutbound = orders_data.get('deviceTrackingOutbound', order.deviceTrackingOutbound)
            order.save()
        return instance
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']