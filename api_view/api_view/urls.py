from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employeeapi/', views.EmployeeApi.as_view()),
    # path('employeeapi/', views.employee_view)
]
