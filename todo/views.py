from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Task

# Create your views here.

def index(request):
    data = Task.objects.order_by('dateToFinish').all()
    context = {
        'data': data
    }
    return render(request, 'index.html', context)

def task(request, id):
    data = get_object_or_404(Task, pk=id)
    context = {
        'data':data
    }
    return render(request, 'task.html', context)