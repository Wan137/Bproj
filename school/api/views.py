from rest_framework.viewsets import ModelViewSet
from ..models import School
from .serializers import SchoolSerializer


class SchoolAPIViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer