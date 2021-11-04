from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.
class Author(models.Model) :
    authorUser = models.OneToOneField(User, on_delete = models.CASCADE)    #связь один к одному c User
    rating = models.IntegerField(default = 0)    #рейтинг пользователя

    def update_rating(self) :
        postRat = self.post_set.all().aggregate(postRating = Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.all().aggregate(commentRating = Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()


class Category(models.Model) :
    article_text = models.CharField(max_length = 123, unique = True)
    subscribers = models.ManyToManyField(User, default='')

class Post(models.Model) :
    postAuthor = models.ForeignKey(Author, on_delete = models.CASCADE)
    NEWS = 'NEWS'
    ARTICLE = 'ARTICLE'
    CHOOSE = (
        (NEWS, 'News'),
        (ARTICLE, 'Article'),
    )
    category_Type = models.CharField(max_length = 123, choices = CHOOSE)
    datetime = models.DateTimeField(auto_now_add = True)
    postCategories = models.ManyToManyField(Category, through = 'PostCategory')
    headline = models.CharField(max_length = 123)
    main_part = models.TextField()
    rating = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.headline}{self.datetime}{self.main_part}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с новостью
        return f'/news/{self.id}'
    
    def like(self) :
        self.rating += 1
        self.save()
    
    def dislike(self) :
        self.rating -= 1
        self.save()

    def preview(self) :
        return self.main_part[0:123] + '...'


class PostCategory(models.Model) :
    postcategoryPost = models.ForeignKey(Post, on_delete = models.CASCADE)
    postcategoryCategory = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model) :
    commentPost = models.ForeignKey(Post, on_delete = models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_text = models.TextField()
    datetime = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)

    def like(self) :
        self.rating += 1
        self.save()

    def dislike(self) :
        self.rating -= 1
        self.save()