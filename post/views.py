from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html')


def new(request):
    return render(request, 'new.html')


def lists(request):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'lists.html', context)


def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.filter(post=post_id)
    context = {
        'post': post,
        'comment': comment
    }
    return render(request, 'detail.html', context)


def create(request):
    title = request.POST['title']
    content = request.POST['content']
    post_active = request.POST['post_active']
    post = Post(title=title, content=content, post_active=post_active, created_at=timezone.now())
    post.save()
    return redirect('post:detail', post_id=post.id)


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post' : post
    }
    return render(request, 'edit.html', context)


def update(request, post_id):
    post = Post.objects.get(id=post_id)
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.post_active = True
    post.save()
    return redirect('post:detail', post_id=post.id)


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('post:lists')


@login_required
def commentcreate(request, post_id):
    user = request.user
    post_id = post_id
    content = request.POST['content']
    comment = Comment(user=user, post_id=post_id, content=content, created_at=timezone.now())
    comment.save()
    return redirect('post:detail', post_id=post_id)


def like(request, post_id):
    if request.method == 'POST':
        try:
            post = Post.objects.get(id=post_id)
            
            if request.user in post.liked_users.all():
                post.liked_users.remove(request.user)
            else:
                post.liked_users.add(request.user)
            return redirect('post:detail', post.id)
        
        except Post.DoseNotExit:
            pass
    return redirect('post:index')
