from django.shortcuts import render
from rest_framework import status
from .permission import IsOwner
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo,UserTradeInfo
from .serializers import UserInfoSerializer,UserTradeInfoSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
# Create your views here.


class UserInfoList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field='user_id'

class UserTradeInfoList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserTradeInfo.objects.all()
    serializer_class = UserTradeInfoSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserTradeInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserTradeInfo.objects.all()
    serializer_class = UserTradeInfoSerializer
    lookup_field='user_id'

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer