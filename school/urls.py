from django.urls import path
from .views import PropertyList, PropertyDetail

urlpatterns = [
    path('school/', PropertyList.as_view(), name='property-list'),
    path('school/<int:pk>/', PropertyDetail.as_view(), name='property-detail'),
]