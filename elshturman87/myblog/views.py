from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Мой блог")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

