from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('UserInfo/', views.UserInfoList.as_view()),
    url(r'^UserInfo/(?P<user_id>\d+)/$', views.UserInfoDetail.as_view()),
    path('UserTradeInfo/', views.UserTradeInfoList.as_view()),
    url(r'^UserTradeInfo/(?P<user_id>\d+)/$', views.UserTradeInfoDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<pk>/', views.UserDetail.as_view()),
]