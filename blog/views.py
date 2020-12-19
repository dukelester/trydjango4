from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create your views here.
from blog.models import Post, DukeLester,Category
from .forms import PostForm


# posts = [
#     {
#         'author': 'duke lester',
#         'title': 'My first post',
#         'content': 'This is very first post',
#         'date_posted': '12,13,2020',
#     },
#     {
#         'author': 'duke lester',
#         'title': 'My first post',
#         'content': 'This is very first post',
#         'date_posted': '12,14,2020',
#     },
#     {
#         'author': 'duke lester',
#         'title': 'My first post',
#         'content': 'This is very first post',
#         'date_posted': '12,15,2020',
#     }
#
# ]
#
#
# def home_view(request):
#     queryset = Post.objects.all()
#
#     context = {
#         'queryset': queryset
#     }
#     return render(request, 'blog/home.html', context)
#
#
# def about_view(request):
#     return render(request, 'blog/about.html')
#
#
# def index_view(request):
#     return render(request, "blog/index.html")
#


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = 'date_posted'


class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'blog/add_category.html'


class BioData(ListView):
    model = DukeLester
    template_name = 'blog/biodata.html'


class MyBiodataView(DetailView):
    model = DukeLester
    template_name = 'blog/mybiodata.html'


class ArticleDetailView(DetailView):
    model = Category
    model = Post
    template_name = 'blog/details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    # fields = '__all__'
    # fields = ('title', 'article', 'author')


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/updatepost.html'
    # fields = ('title', 'content')
    form_class = PostForm


class DeletepostView(DetailView):
    model = Post
    template_name = 'blog/delete-post.html'
    success_url = reverse_lazy('home')
    form_class = PostForm
