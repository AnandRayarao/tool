from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.userlogin, name="userlogin"),
    path("logout/", views.userlogout, name="userlogout")

]