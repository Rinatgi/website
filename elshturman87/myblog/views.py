from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic.base import View
from .models import Post


# Create your views here.
class PostView(View):
    "вывод записей"
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'www/blog.html', {'post_list': posts})


def index(request):
    return render(request, 'www/index.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

