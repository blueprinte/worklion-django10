from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("HELLO WORKS!")

def new(request):
    return HttpResponse("write my posts!")

def lists(request):
    return HttpResponse("my_post lists")