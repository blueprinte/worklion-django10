from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def lists(request):
    context = {
        'title1' : '내가 웹개발을 시작하면서',
        'title2' : '개발에 대해 가지고 있던 생각들',
        'title3' : '하나하나 만들어 가는 내 아이디어',
        'title4' : '무언가를 만들어내기 위해서는 시간이 필요하다.',
    }
    return render(request, 'lists.html', context)