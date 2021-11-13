from django.db import models

class Student(models.Model):
    course_choices = (
    ('1','Java'),
    ('2','Python'),
    ('3','Javascript')
    )
    name = models.CharField(max_length=50)
    rollno = models.IntegerField()
    course = models.CharField(max_length=15,
    choices = course_choices)