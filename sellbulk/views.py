from django.shortcuts import render

# Create your views here.
from .serializers import DevicesSerializer,InquererSerializer, GeneralInquerySerializer
from .models import Inquerer,Devices, GeneralInquery
from rest_framework import generics
from rest_framework import permissions



class InquererListView(generics.ListCreateAPIView):
    permissions_class = [permissions.AllowAny]
    queryset = Inquerer.objects.all()
    serializer_class = InquererSerializer
    #send_email_confirmation(modified=instance)

class GeneralInqueryListView(generics.ListCreateAPIView):
    permissions_class = [permissions.AllowAny]
    queryset = GeneralInquery.objects.all()
    serializer_class = GeneralInquerySerializer
    #send_email_confirmation(modified=instance)