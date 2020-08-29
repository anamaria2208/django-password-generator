from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
  return render(request, 'generator/home.html', {})

def password(request):
  characters = list('abcdefghijklmnopqrstwxyz')
  special = list('!"#$%&/()=?')
  upper = list('ABCDEFGHIJKLMNOPQRSTUWXYZ')
  number = list('0123456789')
  length = int(request.GET.get('length', 12))
  password = ''

  if request.GET.get('uppercase'):
    characters.extend(upper)

  if request.GET.get('special'):
    characters.extend(special)

  if request.GET.get('numbers'):
    characters.extend(number)
  
  for i in range(0, length):
    password += random.choice(characters)

  return render(request, 'generator/password.html', {'password': password})

def about(request):
  return render(request, 'generator/about.html', {})
