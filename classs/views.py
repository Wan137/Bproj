from django.shortcuts import render
from rest_framework import generics
from .models import Class
from .serializers import ClassSerializer



class PropertyList(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer