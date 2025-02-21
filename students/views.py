from django.shortcuts import render, get_object_or_404
from .models import Student

def get_students(request):
    students = Student.objects().all()
    return render(request, 'index.html', {'students': students})

def get_student_by_id(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'index.html', {'students': [student]})