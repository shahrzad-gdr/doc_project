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


