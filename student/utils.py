from django.core.mail import send_mail
from .models import Student

def send_email_to_students(subject, message):
    students = Student.objects.all()
    emails = [student.email for student in students]
    send_mail(subject, message, 'dastan@gmail.com', emails)