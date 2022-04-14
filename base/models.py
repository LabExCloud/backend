from django.db import models


class Department(models.Model):
    department = models.CharField(max_length=50)
    department_code = models.CharField(max_length=4)

    def __str__(self):
        return self.department


class Semester(models.Model):
    semester = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return 'S' + str(self.semester) + ' - ' + self.department.department_code
    

class Subject(models.Model):
    subject = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=6)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.subject