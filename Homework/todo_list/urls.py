from django.urls import path
from todo_list import views

app_name='todo_list'
urlpatterns = [
    # http://127.0.0.1:8000/todo_list/
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('complete/<int:id>', views.complete, name='complete'),
]