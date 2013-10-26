# encoding: utf-8
from django.shortcuts import render, get_object_or_404
from models import Post

def home(request):
    posts = Post.objects.all()
    content = {}
    content['posts'] = posts
    return render(request, 'index.html', content)

def post_detail(request, pk):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, pk=pk)
    context = {}
    context['post'] = post
    return render(request, 'post_detail.html', context)