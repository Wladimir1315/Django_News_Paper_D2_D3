from django.forms import ModelForm
from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):
   # check_box = BooleanField(label='Ало, Галочка!')

    class Meta:
        model = Post
        fields = [ 'post', 'titel_news', 'text_news', 'author', 'category' ]