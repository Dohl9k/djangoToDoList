from django.shortcuts import render, HttpResponseRedirect
from .models import ToDoListItem


# Create your views here.
def todo_view(request):
    all_items = ToDoListItem.objects.all()
    return render(request, 'ToDoApp/todolist.html', {'all_items': all_items})


def add_item(request):
    x = request.POST['content']
    new_item = ToDoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/home/')


def delete_item(request, i):
    y = ToDoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/home/')
