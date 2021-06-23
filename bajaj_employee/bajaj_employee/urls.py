from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('employee', views.EmployeeAPI)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('emp_login/', views.EmployeeLoginAPI.as_view()),
    path('emp_details/', views.EmployeeDetailsAPI.as_view())
]
