from django.db import models


class EmployeeModel(models.Model):
    name = models.CharField(max_length=40)
    emp_id = models.IntegerField()
    city = models.CharField(max_length=40)

