# encoding: utf-8
from django.shortcuts import render
from models import Post

def home(request):
    posts = Post.objects.all()
    content = {}
    content['posts'] = posts
    return render(request, 'index.html', content)