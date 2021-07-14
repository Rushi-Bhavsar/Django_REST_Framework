from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<int:pk>', views.EmployeeApi.as_view()),
    path('api/', views.EmployeeApi.as_view()),
    path('test/', views.TestView.as_view()),
    # path('employeeapi/', views.employee_view)
]

