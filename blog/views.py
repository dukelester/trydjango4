from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from blog.models import Post

posts = [
    {
        'author': 'duke lester',
        'title': 'My first post',
        'content': 'This is very first post',
        'date_posted': '12,13,2020',
    },
    {
        'author': 'duke lester',
        'title': 'My first post',
        'content': 'This is very first post',
        'date_posted': '12,14,2020',
    },
    {
        'author': 'duke lester',
        'title': 'My first post',
        'content': 'This is very first post',
        'date_posted': '12,15,2020',
    }

]


def home_view(request):
    queryset = Post.objects.all()

    context = {
        'queryset': queryset
    }
    return render(request, 'blog/home.html', context)


def about_view(request):
    return render(request, 'blog/about.html')


def index_view(request):
    return render(request, "blog/index.html")
