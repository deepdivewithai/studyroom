from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def room(request):
    return HttpResponse('<h1>Room Page</h1>')