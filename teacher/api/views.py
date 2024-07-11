from rest_framework import generics
from ..models import Teacher
from .serializers import TeacherSerializer, TeacherLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework import permissions


class TeacherRegisterAPIView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = (permissions.IsAuthenticated )

    

    class TeacherLoginAPIView(TokenObtainPairView):
        serializer_class = TeacherLoginSerializer


