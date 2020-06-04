from rest_framework.generics import ListAPIView,RetrieveAPIView
from devices.models import Iphone,Macbook,Ipad,SamsungPhone,GooglePhone
from .serializers import IphoneSerializer, MacbookSerializer,IpadSerializer,SamsungPhoneSerializer,GooglePhoneSerializer

class IphoneListView(ListAPIView):
    queryset=Iphone.objects.all()
    serializer_class=IphoneSerializer

class IphoneDetailView(RetrieveAPIView):
    queryset=Iphone.objects.all()
    serializer_class=IphoneSerializer

class MacbookListView(ListAPIView):
    queryset=Macbook.objects.all()
    serializer_class=MacbookSerializer

class MacbookDetailView(RetrieveAPIView):
    queryset=Macbook.objects.all()
    serializer_class=MacbookSerializer

class IpadListView(ListAPIView):
    queryset=Ipad.objects.all()
    serializer_class=IpadSerializer

class IpadDetailView(RetrieveAPIView):
    queryset=Ipad.objects.all()
    serializer_class=IpadSerializer

class SamsungPhoneListView(ListAPIView):
    queryset=SamsungPhone.objects.all()
    serializer_class=SamsungPhoneSerializer

class SamsungPhoneDetailView(RetrieveAPIView):
    queryset=SamsungPhone.objects.all()
    serializer_class=SamsungPhoneSerializer

class GooglePhoneListView(ListAPIView):
    queryset=GooglePhone.objects.all()
    serializer_class=GooglePhoneSerializer

class GooglePhoneDetailView(RetrieveAPIView):
    queryset=GooglePhone.objects.all()
    serializer_class=GooglePhoneSerializer
