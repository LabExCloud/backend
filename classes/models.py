from django.db import models


class Class(models.Model):
    department = models.ForeignKey('base.Department', on_delete=models.CASCADE)
    semester = models.ForeignKey('base.Semester', on_delete=models.CASCADE)
    subject = models.ForeignKey('base.Subject', on_delete=models.CASCADE)
    batch = models.ForeignKey('base.Batch', on_delete=models.CASCADE)
    owner = models.ForeignKey('user.Teacher', on_delete=models.SET_NULL, null=True)
    teachers = models.ManyToManyField('user.Teacher', related_name='classes')

    models.UniqueConstraint(fields=['department', 'semester', 'subject', 'batch'], name='unique_class')

    def __str__(self):
        return str(self.batch.year) + ' - ' + self.department.dept_code + ' - S' + str(self.semester.sem) + ' - ' + self.subject.sub_name