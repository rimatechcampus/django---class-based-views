from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'post/post_list.html'


class PostDetail(DeleteView):
    model = Post
    template_name = 'post/post_detail.html'


class PostCreate(CreateView):
    pass


class PostDelete(DeleteView):
    pass


class PostUpdate(UpdateView):
    pass
