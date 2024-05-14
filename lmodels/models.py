from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=55)
    age = models.IntegerField()
    dateofbirth = models.DateField()
    studentid = models.CharField(max_length=55, unique=True, null=True)
    city = models.CharField(max_length=55)
    marks  = models.IntegerField()
    join_Date=models.DateField()
