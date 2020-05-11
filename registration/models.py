from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Myuser(User):


    def __str__(self):
        return self.first_name +  self.last_login
