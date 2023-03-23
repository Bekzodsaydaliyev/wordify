from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from blog.models import Article, Tag, Category
from profile.models import Profile


def index(request):
    author = Profile.objects.get()
    articles = Article.objects.all().order_by('-id')
    last_article = Article.objects.order_by('-id')[:1]
    tags = Tag.objects.all()
    categories = Category.objects.all()
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
    paginator = Paginator(articles, 2)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        'object_list': page_obj,
        'author': author,
        'tags': tags,
        'categories': categories,
        'last_article': last_article,
    }
    return render(request, 'wordify/about.html', ctx)
