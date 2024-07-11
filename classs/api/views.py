from rest_framework.viewsets import ModelViewSet
from ..models import Class
from .serializers import ClassSerializer


class ClassAPIViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer