from news.models import User, Author, Category, Post, PostCategory, Comment

user1=User.objects.create(username = 'Ivan')

user2=User.objects.create(username = 'Syva')

author1 = Author.objects.create(users=user1)
author2 = Author.objects.create(users=user2)

category1=Category.objects.create(name_category = 'World cars')
category2=Category.objects.create(name_category = 'Politika')
category3=Category.objects.create(name_category = 'World weather')
category4=Category.objects.create(name_category = 'World music')

post1 = Post.objects.create(author =author1, titel_news = 'О несчастных и счастливых, о добре и зле', text_news = '''Современная христианская музыка — даже не стиль, а смешение самых разнообразных направлений, объединенных общей тематикой. Исполнители в основе песен закрепляют христианские ценности, однако при этом умудряются не скатываться ни в религиозную пропаганду, ни в сектантство. Нет, это не собственно духовная музыка, хотя и в ней, конечно, существуют свои звезды — от хоров различных монастырей до всемирно известных певцов в жанре госпела. Одним из первых христианских музыкальных хитов стала записанная в конце 60-х песня американца Ларри Нормана Why should the devil have all the good music? ("Почему у дьявола вся хорошая музыка?" — Прим. ред.). Музыка того времени со всей ее провокативностью и экспериментальностью ну никак не увязывалась с христианскими традициями. И Норман задал совершенно правильный вопрос: ну, так что же, рокерам вообще нельзя говорить о добре и вечных ценностях, только и надо что воспевать секс да наркотики?''')
post2 = Post.objects.create(author =author1,post = Post.article, titel_news = 'Не злой рок', text_news = 'Сегодня христианская музыка использует любые доступные стили — например, группа As I lay dying играет самый настоящий металкор, весьма суровый, вот только песни проникнуты истинно благостной тематикой.')
post3 = Post.objects.create(author =author1,post = Post.article, titel_news = 'Русские звезды', text_news = 'Есть и у нас весьма успешные христианские коллективы. Первой стала группа "Сыновья России", организованная иеродиаконом Рафаилом')

PostCategory.objects.create(category = category4, post = post1)
PostCategory.objects.create(category = category1, post = post2)
PostCategory.objects.create(category=category3, post=post2)

coment1 = Comment.objects.create(text_comment = 'Это первый очень интересный комент и его я оставлю к первой статье от первого автора', post = post1, userse = user1)
coment2 = Comment.objects.create(text_comment = 'Это второй очень интересный комент и его я оставлю ко второй статье от второго автора', post = post2, userse = user2)
coment3 = Comment.objects.create(text_comment = 'Это третий очень интересный комент и его я оставлю к третей статье от второго автора', post = post3, userse = user2)
coment4 = Comment.objects.create(text_comment = 'Это четвертый очень интересный комент и его я оставлю ко второй статье от первого автора', post = post2, userse = user1)

post1.like()
post2.like()
post3.like()
post2.like()
post1.like()
post2.dislike()
post3.dislike()
coment1.like()
coment2.like()
coment3.like()
coment4.like()
coment1.dislike()
coment4.dislike()

author1.update_rating()
author2.update_rating()

Author.objects.all().order_by('-rating_author').values('users__username','rating_author')[0]

Post.objects.all().order_by('-rating_news').values('time_in','author__users__username','rating_news','titel_news')[0]
Post.objects.all().order_by('-rating_news')[0].preview()

Comment.objects.filter(post=Post.objects.all().order_by('-rating_news')[0]).values('some_datetime', 'userse__username', 'rating_coment', 'text_comment')


