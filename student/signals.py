from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Student

@receiver(post_save, sender=Student)
def send_student_creation_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Добро пожаловать'
        message = f'Здравствуйте, {instance.name}! Вы успешно зарегистрированы.'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [instance.email])