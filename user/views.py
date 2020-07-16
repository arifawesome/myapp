from django.shortcuts import render
from rest_framework import status
from .permission import IsOwner
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo,UserTradeInfo,UserOrder
from .serializers import UserInfoSerializer,UserTradeInfoSerializer,UserSerializer,UserOrderSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
# Create your views here.


class UserInfoList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    filter_backends = [DjangoFilterBackend]

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
    filter_backends = [DjangoFilterBackend]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserTradeInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserTradeInfo.objects.all()
    serializer_class = UserTradeInfoSerializer
    lookup_field='user_id'

class UserOrderList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer
    lookup_field='user_id'

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer