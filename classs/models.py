from django.db import models
from teacher.models import Teacher
from student.models import Student

class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name