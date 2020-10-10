from django.shortcuts import render

# Create your views here.
from .serializers import DevicesSerializer,InquererSerializer
from .models import Inquerer,Devices
from rest_framework import generics
from rest_framework import permissions



class InquererListView(generics.ListCreateAPIView):
    permissions_class = [permissions.AllowAny]
    queryset = Inquerer.objects.all()
    serializer_class = InquererSerializer
    #send_email_confirmation(user=self.request.user, modified=instance)