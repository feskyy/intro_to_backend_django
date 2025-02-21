from django.urls import path
from .views import get_students, get_student_by_id

urlpatterns = [
    path('students', get_students),
    path('students/<int:id>/', get_student_by_id),
]