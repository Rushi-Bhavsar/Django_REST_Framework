from django.contrib import admin
from django.urls import path
from first_drf_get_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_info/<int:roll_no>', views.student_info_selected),
    path('student_info/', views.student_info_selected_by_roll_no)
]
