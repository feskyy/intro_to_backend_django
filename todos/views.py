from django.shortcuts import render
from django.http import JsonResponse
from .models import Todo

def todos_page(request):
    return render(request, "todos/list.html", {"todos": Todo.objects.all()})

def todos_list(request):
    return JsonResponse(list(Todo.objects.values()), safe=False)

def todo_detail(request, id):
    todo = Todo.objects.filter(id=id).first()
    if todo:
        return JsonResponse({
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "due_date": str(todo.due_date),
            "status": todo.status
        })
    return JsonResponse({"error": "Задача не найдена"}, status=404)
