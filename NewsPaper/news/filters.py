from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'time_in':['gt'],
                  'titel_news':['icontains','range'],
                  'author': ['exact'],
                  'rating_news':['icontains'],
                  'post':['exact'],

                  }
