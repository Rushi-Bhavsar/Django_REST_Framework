from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('employee', views.EmployeeAPI)
router.register('employee_punch_in', views.EmployeePunchInAPI)
router.register('employee_punch_out', views.EmployeePunchOutAPI)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
