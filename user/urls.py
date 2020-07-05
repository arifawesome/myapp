from django.urls import path
from . import views

urlpatterns = [
    path('UserInfo/', views.UserInfoList.as_view()),
    path('UserInfo/<pk>/', views.UserInfoDetail.as_view()),
    path('UserTradeInfo/', views.UserTradeInfoList.as_view()),
    path('UserTradeInfo/<pk>/', views.UserTradeInfoDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<pk>/', views.UserDetail.as_view()),
]