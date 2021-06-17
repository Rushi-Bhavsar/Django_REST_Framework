from django.db import models


class StudentModel(models.Model):
    name = models.CharField(max_length=40)
    roll_no = models.IntegerField()
    city = models.CharField(max_length=40)

