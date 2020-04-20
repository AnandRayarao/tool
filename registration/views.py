from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class logiForm(forms.Form):
        username = forms.CharField(label='Email', max_length=100)
        password = forms.CharField(label="Password",widget=forms.PasswordInput)

class MYUserCreationForm(UserCreationForm):


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            print(user, "12345")
            return redirect('/')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

def login(request):
    form = logiForm()
    if request.method == "POST":

    return render(request, "login.html" , {'form':form})