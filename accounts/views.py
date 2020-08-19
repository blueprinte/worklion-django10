from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def sign_up(request):
    context = {}
    
    if request.method == 'POST':
        if (request.POST['username'] and
                request.POST['password'] and
                request.POST['password'] == request.POST['password_check']):
            
            new_user = User.objects.create(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            new_user.save()
            
            auth.login(request, new_user)
            return redirect('index')
    
    return render(request, 'sign_up.html', context)
    
def login(request):
    context = {}

    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:

            user = auth.authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password']
            )

            if user is not None:
                auth.login(request, user)
                return redirect('index')


    return render(request, 'login.html', context)
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        
        
    return redirect('index')