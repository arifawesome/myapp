from django.urls import path
from .views import IphoneListView, IphoneDetailView, MacbookListView, MacbookDetailView

urlpatterns =[
    path('iphoneapi',IphoneListView.as_view()),
    path('iphoneapi/<pk>/',IphoneDetailView.as_view()),
    path('macbookapi/',MacbookListView.as_view()),
    path('macbookapi/<pk>/',MacbookDetailView.as_view())
    
]