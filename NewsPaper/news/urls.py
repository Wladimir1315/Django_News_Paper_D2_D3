from django.contrib import admin
from django.urls import path
from .views import NewsList, PostDetal

urlpatterns = [
    #path('index', index),
    path('', NewsList.as_view()),
    path('<int:pk>', PostDetal.as_view()),

    #path('', PostList.as_view()),



    ]