from django.shortcuts import render, redirect
from .models import Todo
from bs4 import BeautifulSoup

# Create your views here.
def fetching_data():
    todo =  Todo.objects.all().values()
    List = []
    for t in todo:
        List.append((t["content"],t["id"], t["mark"]))
    content ={"todo": List}
    return content

def Todos(request):
    content = fetching_data()
    return render(request, 'Todo.html', content)

def delete(request, id):
    if Todo.objects.filter(id=id).exists():
        Todo.objects.get(id=id).delete()

    return redirect("Todo")


def Add(request):
    if request.method=="POST":
        content = request.POST.get("add")
        if content != "":
            todo = Todo(content = content)
            todo.save()

    return redirect("Todo")


def markAsCompleted(request, id):
    todo = Todo.objects.get(id=id)
    todo.mark = True
    todo.save()
    return redirect('Todo')
