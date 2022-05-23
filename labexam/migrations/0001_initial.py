# Generated by Django 4.0.4 on 2022-05-23 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_alter_user_image'),
        ('classes', '0004_class_unique_class'),
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('total_marks', models.IntegerField()),
                ('class_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab_exams', to='classes.class')),
            ],
        ),
        migrations.CreateModel(
            name='LabExamQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('question', models.TextField(blank=True, max_length=500)),
                ('answer', models.FileField(blank=True, null=True, upload_to='uploads/labexam/correctanswer')),
                ('mark', models.IntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='labexam.labexam')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='editor.language')),
            ],
        ),
        migrations.CreateModel(
            name='LabExamTestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tc_number', models.PositiveIntegerField()),
                ('hidden', models.BooleanField(default=False)),
                ('input_file', models.FileField(upload_to='uploads/labexam/testcase/input')),
                ('output_file', models.FileField(upload_to='uploads/labexam/testcase/output')),
                ('mark', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testcases', to='labexam.labexamquestion')),
            ],
        ),
        migrations.CreateModel(
            name='LabExamAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.FileField(upload_to='uploads/labexam/studentanswer')),
                ('submitted', models.DateTimeField(auto_now_add=True)),
                ('execution_tries', models.IntegerField()),
                ('execution_time', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='labexam.labexamquestion')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
            ],
        ),
        migrations.AddConstraint(
            model_name='labexamanswer',
            constraint=models.UniqueConstraint(fields=('question', 'student'), name='unique_labexam_answer'),
        ),
    ]
