import random
from io import BytesIO
from PIL import Image

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField


class Department(models.Model):
    dept_name = models.CharField(max_length=50, unique=True)
    dept_code = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.dept_name


class Semester(models.Model):
    sem = models.IntegerField(blank=True, unique=True)

    def __str__(self):
        return 'S' + str(self.sem)


class Batch(models.Model):
    class Stream(models.TextChoices):
        BTECH = 'B.Tech', _('B.Tech')
        MTECH = 'M.Tech', _('M.Tech')
    
    year = models.IntegerField()
    stream = models.CharField(max_length=8, choices=Stream.choices, default=Stream.BTECH)
    models.UniqueConstraint(fields=['year', 'stream'], name='unique_batch')

    def __str__(self):
        return str(self.year) + ' - ' + self.stream
    

class Subject(models.Model):
    sub_name = models.CharField(max_length=100)
    sub_code = models.CharField(max_length=6, unique=True)
    image = ResizedImageField(size=[400, 400], upload_to='uploads/subjects/', blank=True, null=True)
    
    def __str__(self):
        return self.sub_name