from django.db import models


class Student(models.Model):
    studentID = models.PositiveSmallIntegerField(primary_key=True)
    firstName = models.TextField(max_length=15, default="Enter first name... ")
    lastName = models.TextField(max_length=15, default="Enter last name... ")
    studentEmail = models.EmailField(blank=True)
    studentAge = models.IntegerField(default="Enter student age... ")
    studentGrade = models.IntegerField(default="Enter student grade... ")
