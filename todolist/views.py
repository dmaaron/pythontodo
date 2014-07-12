from django.shortcuts import render
from todolist.models import Task
# Create your views here.
def tasks(request):
    template_name='tasks.html'
    tasks=Task.objects.all()
    context={'tasks':tasks}
    return render(request, template_name, context)