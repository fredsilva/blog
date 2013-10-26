# encoding: utf-8
from django.shortcuts import render, get_object_or_404
from models import Post
from forms import CommentForm

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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            context['form'] = CommentForm()
            return render(request, 'post_detail.html', context)
    else:
        form = CommentForm()
    context['form'] = form
    return render(request, 'post_detail.html', context)