from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from django.core.mail import send_mail
from django.conf import settings
from .models import Student

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def send_email_to_students(subject, message):
    #     students = Student.objects.all()
    #     emails = [student.email for student in students]
    #     send_mail(subject, message, settings.EMAIL_HOST_USER, emails)
