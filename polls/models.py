from django import forms
from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    student_id = models.IntegerField(verbose_name='شماره دانشجویی')
    is_student = models.BooleanField()


class Person(models.Model):
    national_id = models.IntegerField()
    age = models.IntegerField()


class DaySelection(models.Model):
    day = models.CharField(max_length=256)


class Article(models.Model):
    department = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=250)
    start_time = models.TimeField()
    end_time = models.TimeField()
