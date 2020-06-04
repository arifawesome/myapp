from django.urls import path
from .views import IphoneListView, IphoneDetailView, MacbookListView, MacbookDetailView,IpadListView,IpadDetailView,SamsungPhoneListView,SamsungPhoneDetailView,GooglePhoneListView,GooglePhoneDetailView

urlpatterns =[
    path('iphoneapi',IphoneListView.as_view()),
    path('iphoneapi/<pk>/',IphoneDetailView.as_view()),
    path('macbookapi/',MacbookListView.as_view()),
    path('macbookapi/<pk>/',MacbookDetailView.as_view()),
    path('ipadapi',IpadListView.as_view()),
    path('ipadapi/<pk>/',IpadDetailView.as_view()),
    path('samsungapi/',SamsungPhoneListView.as_view()),
    path('samsungapi/<pk>/',SamsungPhoneDetailView.as_view()),
    path('googleapi/',GooglePhoneListView.as_view()),
    path('googleapi/<pk>/',GooglePhoneDetailView.as_view())
    
]