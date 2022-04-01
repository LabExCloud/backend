from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    rollno = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()