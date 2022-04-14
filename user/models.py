from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    rollno = models.IntegerField(blank=True, null=True)
    semester = models.ForeignKey('base.Semester', on_delete=models.CASCADE)
    department = models.ForeignKey('base.Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    department = models.ForeignKey('base.Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Teacher.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()