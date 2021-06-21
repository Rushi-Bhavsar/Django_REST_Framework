from django.db import models
from datetime import time


class EmployeeModel(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.emp_id}"


class EmployeePunchInModel(models.Model):
    punch_in = models.TimeField()
    emp_id = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)


class EmployeePunchOutModel(models.Model):
    punch_out = models.TimeField()
    emp_id = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
