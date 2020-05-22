import json

from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import models


# Create your views here.
from django.utils.safestring import mark_safe

from instagram.models import Article, ArticleComments


class addArticleForm(forms.ModelForm):
        author = forms.HiddenInput()
        class Meta:

          model = Article
          fields = ['name', 'description']


def index(request):
        articles = Article.objects.all()
        for x in articles:
            for  a in x.comments.all():
                print(a.user.id)

        return render(request, "base.html",{"article":articles})


def add_article(request):
    if request.method == "POST":

        form = addArticleForm(request.POST)
        if form.is_valid():
            name = str(form['name'].value())
            description = str(form['description'].value())
            article = Article(name=name,description = description,author = request.user)
            article.save()
            return redirect("/")

        return render(request, "add_article.html", {"form": form})

    else:
        form = addArticleForm(request.POST)
        return render(request, "add_article.html", {"form": form})

def like_article(request,id):
    status = ""
    article = Article.objects.get(pk=id)
    if request.user in article.likes.all():
        status = "unliked"
        article.likes.remove(request.user.id)
    else:

        status = "liked"
        article.likes.add(request.user.id)

    return HttpResponse(json.dumps({"likes":article.likes.count(),
                                "status":status}))

def viewauthor(request,id):
    user  = User.objects.get(pk = id)
    articles = Article.objects.filter(author = user)


    return render(request,"authorview.html",({'author':user,
                                             "articles":(articles)}))


class commentForm(forms.Form):
        comment = forms.CharField(label='comment', max_length=100,
                                   widget=forms.TextInput(attrs={'class':'form-control'}))

def viewarticle(request,id):
    form = commentForm()
    if request.method == 'POST':
        form = commentForm(request.POST)
        article = Article.objects.get(pk=id)
        if form.is_valid():
          comment = form.cleaned_data['comment']
          print(request.user.id)
          article_comment = ArticleComments(comment = comment,
                                            user=request.user)
          article_comment.save()
          article.comments.add(article_comment)

          return redirect('/article/' + id)
    else:
        article = Article.objects.get(pk=id)
        return render(request, "article.html",{'article':article,'form':form})