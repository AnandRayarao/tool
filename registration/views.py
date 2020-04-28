from django.contrib.auth.models import User
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UsernameField


# Create your views here.

class logiForm(forms.Form):
        username = forms.CharField(label='username', max_length=100)
        password = forms.CharField(label="Password",widget=forms.PasswordInput)

class MYUserCreationForm(forms.Form):
    firstname = forms.CharField(label='Firstname', max_length=100)
    lastname = forms.CharField(label='Lastname', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    email = forms.CharField(label='Email',widget=forms.EmailInput)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Conform password",
                                widget=forms.PasswordInput)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = MYUserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'],
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            user = User.objects.create_user(form.cleaned_data['username'],
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            user.save()

            return redirect("/user/login")
    else:
        form = MYUserCreationForm()
        return render(request, 'register.html', {'form': form})

def userlogin(request):

    if request.method == "POST":
        form = logiForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
             login(request, user)
             return redirect('/')
    else:
     form = logiForm()
     return render(request, "login.html" , {'form':form})

def userlogout(request):

    logout(request)
    return redirect("/")