from django.db import models


# Create your models here.
class Course(models.Model):
    number = models.CharField('Номер документа', max_length=50)


class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.CharField('Номер раздела', max_length=50)
