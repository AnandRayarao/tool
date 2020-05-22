from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UsernameField


# Create your views here.

class logiForm(forms.Form):
        username = forms.CharField(label='Username', max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
        password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))

class MYUserCreationForm(UserCreationForm):
    firstname = forms.CharField(label='Firstname', max_length=100)
    lastname = forms.CharField(label='Lastname', max_length=100)
    email = forms.CharField(label='Email', widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ("firstname", "lastname", "email","username",)
        field_classes = {'username': UsernameField}




def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = MYUserCreationForm(request.POST)
        if form.is_valid():

            form.save()

            return redirect("/user/login")
        return render(request, 'register.html', {'form': form})
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