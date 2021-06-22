from django.contrib import admin
from .models import EmployeeModel, EmployeeLoginModel, EmployeeDetailsModel


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'emp_id', 'city']


@admin.register(EmployeeLoginModel)
class EmployeeLoginAdmin(admin.ModelAdmin):
    list_display = ['id', 'punch_in', 'punch_out', 'employee']


@admin.register(EmployeeDetailsModel)
class EmployeeDetailAdmin(admin.ModelAdmin):
    list_display = ['emp_name', 'emp_id', 'working_hours']
