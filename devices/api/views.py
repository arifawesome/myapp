from rest_framework.generics import ListAPIView,RetrieveAPIView
from devices.models import Iphone,Macbook
from .serializers import IphoneSerializer, MacbookSerializer

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
