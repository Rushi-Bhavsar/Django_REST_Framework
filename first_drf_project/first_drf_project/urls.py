from django.contrib import admin
from django.urls import path
from first_drf_get_api import views as get_view
from drf_create_api import views as create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_info/<int:roll_no>', get_view.student_info_selected),
    path('student_info/', get_view.student_info_selected_by_roll_no),
    path('student_create/', create_view.student_create),
]
