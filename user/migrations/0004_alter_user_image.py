# Generated by Django 4.0.4 on 2022-05-02 06:46

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[400, 400], upload_to='uploads/profile/'),
        ),
    ]