from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

from base.models import Department, Semester, Batch, Class


class User(AbstractUser):
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profile/', blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    rollno = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return self.user.username

@receiver(post_delete, sender=Student)
def auto_delete_user_with_profile(sender, instance, **kwargs):
    instance.user.delete()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return self.user.username


@receiver(post_delete, sender=Teacher)
def auto_delete_user_with_profile(sender, instance, **kwargs):
    instance.user.delete()
