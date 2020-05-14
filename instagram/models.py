from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class ArticleComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    added_date = models.DateField(auto_now=True)


class Article(models.Model):
    name = models.CharField(max_length = 80)
    description = models.TextField(max_length = 500)
    author = models.ForeignKey(User,on_delete=models.CASCADE,
                               related_name="author")
    likes = models.ManyToManyField(User, related_name="likes")
    comments = models.ManyToManyField(ArticleComments,related_name="comments")




