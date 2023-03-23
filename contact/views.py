from django.shortcuts import render, redirect
from .models import Contact
from blog.models import Article, Tag, Category
from profile.models import Profile
from .forms import ContactForm


def index(request):
    last_article = Article.objects.get(id=1)
    author = Profile.objects.get()
    articles = Article.objects.all()
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
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact:index")
    ctx = {
        'form': form,
        'author': author,
        'articles': articles,
        'last_article': last_article,
        'tags': tags,
        'categories': categories,
    }
    return render(request, 'wordify/contact.html', ctx)