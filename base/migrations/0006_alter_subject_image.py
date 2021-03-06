# Generated by Django 4.0.4 on 2022-05-25 17:48

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_batch_unique_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=90, size=[400, 400], upload_to='uploads/subjects/'),
        ),
    ]
