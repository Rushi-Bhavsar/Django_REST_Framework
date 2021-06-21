from django.contrib import admin
from .models import EmployeeModel


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'emp_id', 'city']
