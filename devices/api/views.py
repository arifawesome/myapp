from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from devices.models import Iphone,Macbook,Ipad,SamsungPhone,GooglePhone,Ipod,Iwatch,Devices
from .serializers import IphoneSerializer, MacbookSerializer,IpadSerializer,SamsungPhoneSerializer,GooglePhoneSerializer, IpodSerializer, IwatchSerializer, DevicesSerializer
from django_filters.rest_framework import DjangoFilterBackend

class IphoneListView(ListAPIView):
    queryset=Iphone.objects.all()
    serializer_class=IphoneSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class IphoneDetailView(RetrieveAPIView):
    queryset=Iphone.objects.all()
    serializer_class=IphoneSerializer
    

class MacbookListView(ListAPIView):
    queryset=Macbook.objects.all()
    serializer_class=MacbookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class MacbookDetailView(RetrieveAPIView):
    queryset=Macbook.objects.all()
    serializer_class=MacbookSerializer

class IpadListView(ListAPIView):
    queryset=Ipad.objects.all()
    serializer_class=IpadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class IpadDetailView(RetrieveAPIView):
    queryset=Ipad.objects.all()
    serializer_class=IpadSerializer
    

class SamsungPhoneListView(ListAPIView):
    queryset=SamsungPhone.objects.all()
    serializer_class=SamsungPhoneSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class SamsungPhoneDetailView(RetrieveAPIView):
    queryset=SamsungPhone.objects.all()
    serializer_class=SamsungPhoneSerializer

class GooglePhoneListView(ListAPIView):
    queryset=GooglePhone.objects.all()
    serializer_class=GooglePhoneSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class GooglePhoneDetailView(RetrieveAPIView):
    queryset=GooglePhone.objects.all()
    serializer_class=GooglePhoneSerializer

class IpodListView(ListAPIView):
    queryset=Ipod.objects.all()
    serializer_class=IpodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class IpodDetailView(RetrieveAPIView):
    queryset=Ipod.objects.all()
    serializer_class=IpodSerializer

class IwatchListView(ListAPIView):
    queryset=Iwatch.objects.all()
    serializer_class=IwatchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class IwatchDetailView(RetrieveAPIView):
    queryset=Iwatch.objects.all()
    serializer_class=IwatchSerializer

class DevicesListView(ListAPIView):
    queryset=Devices.objects.all()
    serializer_class=DevicesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class DevicesDetailView(RetrieveAPIView):
    queryset=Devices.objects.all()
    serializer_class=DevicesSerializer

