from django.db import models
from classs.models import Class

class School(models.Model):
    name = models.CharField(max_length=255)
    classes = models.ManyToManyField(Class)

    class Meta:
        verbose_name = "Школа"       
    def __str__(self):
            return self.name