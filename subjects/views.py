from django.shortcuts import render, get_object_or_404
from .apps import SubjectsConfig
from .models import Course



def get_subjects(request):
    course = Course.objects().all()
    return render(request, 'index.html', {'subjects': course})

def get_course_by_id(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'index.html', {'course': course})