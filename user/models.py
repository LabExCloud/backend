from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField


class User(AbstractUser):
    class UserType(models.TextChoices):
        STUDENT = 'student', _('Student')
        TEACHER = 'teacher', _('Teacher')
        ADMIN = 'admin', _('Admin')
    
    user_type = models.CharField(max_length=8, choices=UserType.choices)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    image = ResizedImageField(size=[400, 400], upload_to='uploads/profile/', blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)


class Student(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True,)
    rollno = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey('base.Department', on_delete=models.PROTECT)
    semester = models.ForeignKey('base.Semester', on_delete=models.PROTECT)
    batch = models.ForeignKey('base.Batch', on_delete=models.CASCADE)
    classes = models.ManyToManyField('classes.Class')

    def __str__(self):
        return self.user.username

@receiver(post_delete, sender=Student)
def auto_delete_user_with_profile(sender, instance, **kwargs):
    instance.user.delete()


class Teacher(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True,)
    department = models.ForeignKey('base.Department', on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username


@receiver(post_delete, sender=Teacher)
def auto_delete_user_with_profile(sender, instance, **kwargs):
    instance.user.delete()
