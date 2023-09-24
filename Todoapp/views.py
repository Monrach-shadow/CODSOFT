from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def Todos(request):
    todo =  Todo.objects.all().values()
    List = []
    for t in todo:
        List.append((t["content"],t["id"]))
    content ={"todo": List}
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
