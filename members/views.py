from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from blog.models import Post


class UserRegisterView(generic.CreateView):

    from_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
