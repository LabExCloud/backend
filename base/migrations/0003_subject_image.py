# Generated by Django 4.0.4 on 2022-05-02 07:26

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_department_dept_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[512, 512], upload_to='uploads/subjects/'),
        ),
    ]
