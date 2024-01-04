from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods

from todo.models import Todo


def home(request):
    todos = Todo.objects.all()
    print("--->To Do's: %s" % (todos))

    return render(request, 'index.html', {"todos" : todos})



@require_http_methods(['POST'])
def add(request):
    title = request.POST.get('title')

    if title:
        todo = Todo.objects.create(title=title)
        todo.save()
        print("--->Todo: %s" % (todo))

    return render(request, "partials/todo.html", {"todo" : todo})


@require_http_methods(['PUT'])
def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = True
    todo.save()

    return render(request, 'partials/todo.html', {'todo' : todo})


@require_http_methods(['DELETE'])
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return HttpResponse()