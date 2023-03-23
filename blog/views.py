from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article, Category, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from profile.models import Profile
from .forms import CommentForm


def index(request):
    author = Profile.objects.get(id=1)
    last_article = Article.objects.get(id=1)
    articles = Article.objects.order_by('-id')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if search:
        articles = articles.filter(title__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 4)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)

    ctx = {
        'object_list': page_obj,
        'categories': categories,
        'tags': tags,
        'author': author,
        'last_article': last_article,
        # 'search': search,
    }
    return render(request, 'wordify/index.html', ctx)


def article_list(request):
    author = Profile.objects.get(id=1)
    last_article = Article.objects.get(id=1)
    object_list = Article.objects.all().order_by('-id')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if tag:
        object_list = object_list.filter(tags__title__exact=tag)
    if cat:
        object_list = object_list.filter(category__title__exact=cat)
    if search:
        object_list = object_list.filter(title__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(object_list, 4)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        'object_list': page_obj,
        'tags': tags,
        'last_article': last_article,
        'categories': categories,
        'author': author,
    }
    return render(request, 'wordify/blog.html', ctx)


def article_detail(request, pk):
    author = Profile.objects.get(id=pk)
    last_article = Article.objects.get(id=1)
    articles = get_object_or_404(Article, id=pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if not request.user.is_authenticated:
            return redirect("account:login")
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.profile.id
            obj.article_id = articles.id
            obj.save()
            return redirect('.')
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if search:
        articles = articles.filter(title__icontains=search)
    ctx = {
        'cat': cat,
        'search': search,
        'articles': articles,
        'tags': tags,
        'categories': categories,
        'last_article': last_article,
        'author': author,
        'form': form,
    }
    return render(request, 'wordify/blog-single.html', ctx)


def nav_views(request):
    article = Article.objects.order_by('-id')
    categories = Category.objects.all()
    cat = request.GET.get('cat')
    if cat:
        article = article.filter(category__title__exact=cat)
    ctx = {
        'cat': cat,
        'article': article,
        'categories': categories,
    }
    return render(request, 'nav.html', ctx)


def category_view(request):
    author = Profile.objects.get()
    article = Article.objects.order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat = request.GET.get('cat')
    last_article = Article.objects.order_by('-id')[:3]
    if cat:
        article = article.filter(category__title__exact=cat)
    ctx = {
        'last_article': last_article,
        'author': author,
        'cat': cat,
        'articles': article,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'wordify/category.html', ctx)
