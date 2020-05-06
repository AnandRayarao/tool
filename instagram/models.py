from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length = 80)
    description = models.TextField(max_length = 500)
    author  = models.ForeignKey(User,on_delete=models.CASCADE)
