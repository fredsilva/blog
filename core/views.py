# encoding: utf-8
from django.shortcuts import render, get_object_or_404
from models import Post
from forms import CommentForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    posts = Post.objects.all()
    search = request.GET.get('search','')
    if search:
        posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
    #paginação
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    #fim da paginação
    context = {}
    context['posts'] = posts
    context['search'] = search
    return render(request, 'index.html', context)

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