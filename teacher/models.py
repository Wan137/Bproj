from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class TeacherManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)


class Teacher(AbstractUser):
    username = None
    email = None
    phone_number = models.CharField(unique=True, max_length=15)
    class_name = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    # first_name = models.CharField(max_length=30, verbose_name='Имя')
    # last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    # phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', unique=True)
    # classroom = models.CharField(max_length=50, verbose_name='Класс')
    # subject_name = models.CharField(max_length=100, verbose_name='Название предмета')
    # is_active = models.BooleanField(default=True, verbose_name='Активный')
    # is_staff = models.BooleanField(default=False, verbose_name='Персонал')

    objects = TeacherManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

