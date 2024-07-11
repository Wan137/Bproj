from django.urls import path
from .views import PropertyList, PropertyDetail

urlpatterns = [
    path('class/', PropertyList.as_view(), name='property-list'),
    path('class/<int:pk>/', PropertyDetail.as_view(), name='property-detail'),
]