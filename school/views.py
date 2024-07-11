from django.shortcuts import render
from rest_framework import generics
from .models import School
from school.api.serializers import SchoolSerializer



class PropertyList(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer