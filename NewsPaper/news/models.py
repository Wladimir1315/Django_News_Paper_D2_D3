from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):

    rating_author =models.FloatField(default = 0)

    users = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)

    def __str__(self):
        return f'{self.users.username}'

    def update_rating(self):
        post_auth = Post.objects.filter(author=self.id)
        value_post=sum([r.rating_news for r in post_auth])  # Каждой статьи автора
        value_post = value_post * 3
        value_auth = sum([r['rating_coment'] for r in Comment.objects.filter(userse=self.users).values('rating_coment')])  # всех комментариев автора
        value_comment = sum([r['rating_coment'] for r in Comment.objects.filter(post__in=post_auth).values('rating_coment')])
        self.rating_author = value_post + value_auth + value_comment
        self.save()






class Category(models.Model):
    name_category = models.CharField(max_length = 255, unique = True)

    def __str__(self):
        return f'{self.name_category}'


class Post(models.Model):

    news = 'NW'
    article = 'AC'

    POSTS = (
        (news,'Новость'),
        (article, 'Статья')
    )
    post=models.CharField(max_length = 20,
                            choices = POSTS,
                            default = news)


    time_in = models.DateTimeField(auto_now_add=True)
    titel_news = models.CharField(max_length = 255)
    text_news = models.TextField()
    rating_news = models.IntegerField(default = 0)

    author = models.ForeignKey(Author,on_delete = models.CASCADE)
    category = models.ManyToManyField(Category, through ='PostCategory')

    def __str__(self):
        return f'{self.titel_news}'

    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'

    def like(self):
        self.rating_news += 1
        self.save()

    def dislike(self):
        self.rating_news -= 1
        self.save()

    def preview(self):
        priviews_ = self.text_news[:124]
        return priviews_+'...'

class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):


    text_comment = models.TextField()
    some_datetime = models.DateTimeField(auto_now_add=True)
    rating_coment = models.IntegerField(default = 0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    userse = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text_comment}'



    def like(self):
        self.rating_coment += 1
        self.save()

    def dislike(self):
        self.rating_coment -= 1
        self.save()







