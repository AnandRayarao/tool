from django.contrib import admin

# Register your models here.
from instagram.models import Article, ArticleComments

admin.site.register(Article)
admin.site.register(ArticleComments)