from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee_api/', views.EmployeeListCreate.as_view()),
    path('employee_api/<int:pk>', views.EmployeeRetrieveUpdateDelete.as_view())
]
