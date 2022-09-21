from django.views.generic import ListView
from .models import ToDoList


# Create your views here.
class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"