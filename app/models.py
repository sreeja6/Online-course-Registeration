from django.db import models

from django.db import models
class Course(models.Model):
    No = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Faculty = models.CharField(max_length=30)
    Date = models.CharField(max_length=20)
    Time = models.CharField(max_length=20)
    Fee = models.IntegerField()
    Duration = models.CharField(max_length=30)

class Student(models.Model):
    No = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30, unique=True)
    Contact = models.IntegerField(unique=True)
    Email = models.EmailField(unique=True)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
class EnrolledStudents(models.Model):
    e_id = models.IntegerField()
    e_name = models.CharField(max_length=20)
    e_course = models.CharField(max_length=20)
    e_faculty = models.CharField(max_length=20)


