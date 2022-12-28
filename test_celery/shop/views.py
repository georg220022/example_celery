from cgi import test
from turtle import delay
from django.http import HttpResponse
from .tasks import test_task

def pages(request, *args, **kwargs):
    test_task.delay("Прокинутый аргумент")
    return HttpResponse(status=200)
    