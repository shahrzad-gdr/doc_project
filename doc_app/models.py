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
    status  = models.CharField(max_length=1, choices=COURSE_STATUS.choices)

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
    gender = models.CharField(max_length=1, choices=GENDER_TYPE.choices, default='F')

    def __str__(self):
        return self.first_name , self.last_name



class Submitted_Course(models.Model):
    class Meta:
        verbose_name = 'Submitted_Course'
        verbose_name_plural = 'Submitted_Courses'

    class GENDER_TYPE(models.TextChoices):
        FEMALE = 'F', 'Mrs.'    # if you need persian values: FEMALE = 'F', 'زن'
        MALE = 'M', 'Mr.'       # if you need persian values: MALE = 'M', 'مرد'

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='student')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='course')
    submit_date = models.DateField(auto_now_add=True, verbose_name='date')


    def __str__(self):
        return self.student


class Result(models.Model):
    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Results'

    class STATUS_TYPE(models.TextChoices):
        EDUCATE = 'E', 'Educate'
        GRADUATE = 'G', 'Graduate'
        CANCEL = 'C', 'Cancel'

    class GRADE_TYPE(models.TextChoices):  # or you can ignore choice and consider a decimalField for grade
        A = 'A', 'A'
        B = 'B', 'B'
        C = 'C', 'C'

    submitted_course = models.OneToOneField(Submitted_Course, on_delete=models.CASCADE, verbose_name='submitted course')
    status = models.CharField(max_length=1, default='E', choices=STATUS_TYPE.choices, verbose_name='status')
    # grade  = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,  verbose_name='grade')
    grade = models.CharField(max_length=1, blank=True, null=True, choices=GRADE_TYPE.choices, verbose_name='grade')
    validation = models.ImageField(upload_to='media/validation/', verbose_name='validation', blank=True, null=True)

    def __str__(self):
        return self.submitted_course.student, self.submitted_course.course

