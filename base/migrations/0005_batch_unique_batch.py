# Generated by Django 4.0.4 on 2022-05-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_subject_image'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='batch',
            constraint=models.UniqueConstraint(fields=('year', 'stream'), name='unique_batch'),
        ),
    ]
