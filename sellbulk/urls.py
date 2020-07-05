from django.urls import path,include
from .views import InquererListView

urlpatterns=[
    path('/inquerer', InquererListView.as_view())
]