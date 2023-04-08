import datetime
import os
import uuid

from django.contrib.auth.models import User
from django.db import models




class Academy(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


    name         = models.CharField(max_length=20, verbose_name='academy')
    manager_name = models.CharField(max_length=50, verbose_name='name')
    logo         = models.ImageField(upload_to='media/logo/', verbose_name='logo')


    def __str__(self):
        return self.name



class Course(models.Model):
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    class COURSE_STATUS(models.TextChoices):
          AVAILABLE = 'A', 'Available'
          EXPIRED = 'E', 'Expired'


    academy = models.ForeignKey(Academy, on_delete=models.CASCADE, verbose_name='academy')
    name    = models.CharField(max_length=20, verbose_name='course')
    status  = models.CharField(max_length=1, choices=COURSE_STATUS)

    def __str__(self):
        return  self.name




class Student(models.Model):
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    class GENDER_TYPE(models.TextChoices):
        FEMALE = 'F', 'Mrs.'    # if you need persian values: FEMALE = 'F', 'زن'
        MALE = 'M', 'Mr.'       # if you need persian values: MALE = 'M', 'مرد'

    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='student')
    first_name = models.CharField(max_length=20, verbose_name='first name')
    last_name = models.CharField(max_length=20, verbose_name='last name')
    gender = models.CharField(max_length=1, choices=GENDER_TYPE, default='F')

    def __str__(self):
        return self.first_name , self.last_name


