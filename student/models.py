from django.db import models
from teacher.models import Teacher

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField()
    birth_date = models.DateField()
    grade = models.CharField(max_length=11, verbose_name='Класс')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], verbose_name='Пол')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students')


    class Meta:
        verbose_name = "Студент"
        
    def __str__(self):
            return self.name
