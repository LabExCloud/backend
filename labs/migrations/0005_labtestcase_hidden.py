# Generated by Django 4.0.4 on 2022-05-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0004_alter_labquestion_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtestcase',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
