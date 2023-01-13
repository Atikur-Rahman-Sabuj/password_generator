from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'home.html', {'password': 'kjwheijwqk'})


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    password = ''
    for x in range(int(request.GET.get("length", 8))):
        password += random.choice(characters)

    return render(request, 'password.html', {'password': password})
