from django.contrib import admin
from todo_app.models import ToDoList, ToDoItem


# Register your models here.
admin.site.register(ToDoList)
admin.site.register(ToDoItem)
