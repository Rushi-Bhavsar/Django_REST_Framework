from django.contrib import admin
from .models import EmployeeModel, EmployeePunchInModel, EmployeePunchOutModel


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'emp_id', 'city']


@admin.register(EmployeePunchInModel)
class EmployeePunchInAdmin(admin.ModelAdmin):
    list_display = ['id', 'emp_id', 'punch_in']


@admin.register(EmployeePunchOutModel)
class EmployeePunchOutAdmin(admin.ModelAdmin):
    list_display = ['id', 'emp_id', 'punch_out']
