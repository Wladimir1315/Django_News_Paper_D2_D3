from django.contrib import admin
from django.urls import path
from .views import NewsList, PostSearch, PostCreateView, PoctDeteil, PostDeleteView, PostUpdateView

urlpatterns = [

    path('', NewsList.as_view(), name='news'),
    path('<int:pk>/', PoctDeteil.as_view(),name='post_detail'),
    path('search/', PostSearch.as_view()),
    path('add/', PostCreateView.as_view(), name='post_add'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/updete/', PostUpdateView.as_view(), name='post_update'),






    ]