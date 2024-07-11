from rest_framework.viewsets import ModelViewSet
from ..models import Student
from .serializers import StudentSerializer
import django_filters
# from rest_framework import permissions


class StudentAPIViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['name', 'email']
    # permission_classes = (permissions.IsAuthenticated, )

