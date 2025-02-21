from django.urls import path
from .views import get_subjects, get_course_by_id

urlpatterns = [
    path('courses/', get_subjects),
    path('courses/<int:id>/', get_course_by_id),
]