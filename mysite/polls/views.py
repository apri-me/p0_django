from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index_view(request):
    return HttpResponse("<h1>Hello world</h1>")

def second_view(request):
    return HttpResponse("<h2>Salam</h2>")