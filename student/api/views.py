from rest_framework.viewsets import ModelViewSet
from ..models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from ..filters import StudentFilter
from rest_framework import generics
# import django_filters
# from rest_framework import permissions


class StudentAPIViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter

# class StudentFilter(django_filters.FilterSet):
#     class Meta:
#         model = Student
#         fields = ['name', 'email']
    # permission_classes = (permissions.IsAuthenticated, )

