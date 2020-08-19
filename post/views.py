from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def lists(request):
    post = Post.objects.all()
    context = {
        'post' : post
    }
    return render(request, 'lists.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post' : post
    }
    return render(request, 'detail.html', context)

def create(request):
    title = request.POST['title']
    content = request.POST['content']
    post_active = request.POST['post_active']
    post = Post(title=title, content=content, post_active=post_active, created_at=timezone.now())
    post.save()
    return redirect('post:detail', post_id = post.id)