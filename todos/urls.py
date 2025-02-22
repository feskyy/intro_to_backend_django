from django.urls import path
from .views import todos_list, todo_detail, todos_page

urlpatterns = [
    path('', todos_list),
    path('<int:id>/', todo_detail),
    path('', todos_page)
]
