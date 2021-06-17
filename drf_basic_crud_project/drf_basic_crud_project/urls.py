from django.contrib import admin
from django.urls import path
from basic_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/<int:roll_no>', views.student_info),
    path('studentapi/', views.student_info),
    # path('studentapi/', views.StudentView.as_view()),
]
