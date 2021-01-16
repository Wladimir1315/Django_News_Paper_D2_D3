#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, Comment

class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'post'
    queryset = Post.objects.order_by('-id')

class PostDetal(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


