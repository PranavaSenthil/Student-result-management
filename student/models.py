from django.db import models
from django.conf import settings

# Create your models here.
class year(models.Model):
    Sno = models.IntegerField(null=True,blank=True)
    year = models.CharField(max_length=20,null=True, blank=True)
    dept = models.CharField(max_length=30)

class subject(models.Model):
    Sno = models.IntegerField(null=True,blank=True)
    code = models.IntegerField()
    subjects = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

class student(models.Model):
    Sno = models.IntegerField(null=True,blank=True)
    student_ID = models.IntegerField(primary_key=True)
    gender = models.CharField(
        max_length=6,
        choices=[('MALE', 'MALE'),('FEMALE', 'FEMALE')]
    )
    name = models.CharField(max_length=50,null=True,blank=True)
    Address = models.TextField()
    year = models.CharField(max_length=20)

class result(models.Model):
    Sno = models.IntegerField(null=True,blank=True)
    student_ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    semester = models.ForeignKey(year,default=1,on_delete=models.SET_DEFAULT)
    subjects = models.ForeignKey(subject,default=1,on_delete=models.SET_DEFAULT)
    grade = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
