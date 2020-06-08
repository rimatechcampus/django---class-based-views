from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.
from .models import Post


class PostList(ListView):
    model = Post
    # template_name = 'post/post_list.html'
    # context_object_name = 'all_posts'
    ordering = ['-created_at']
    # queryset = Post.objects.filter(active=True)

    def get_queryset(self):
        return Post.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = 'sophie'
        context['lname'] = 'ro'
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'


class PostCreate(CreateView):
    pass


class PostDelete(DeleteView):
    pass


class PostUpdate(UpdateView):
    pass
