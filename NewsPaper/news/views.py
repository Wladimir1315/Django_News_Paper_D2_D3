from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.views import View

from .models import Author, Category, Post, Comment
from .filters import PostFilter
from .forms import PostForm


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'post'
    ordering = ['-id']
    paginate_by = 2

class PoctDeteil(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()


class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'post'
    ordering = ['-id']
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET,queryset=self.get_queryset())
        return context

class PostCreateView(CreateView):
    model = Post
    template_name = 'news/add_news.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/add_news.html'



    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'



