from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from .models import Contact ,Article, Category, Section

# Create your views here.

# article category page
def article_category(request, slug):
    articles = Article.objects.filter(category__name = slug)
    categories = Category.objects.all()
    return render(request,'articles/article_category.htm',{'articles':articles,'categories':categories})

# article list page
def article_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,'articles/article_list.htm',{'articles':articles})

# article details
def article_details(request,slug):
    article = Article.objects.get(slug=slug)
    stories = Article.objects.all().order_by('date')[:4]
    sections = Section.objects.filter(root_article=article)
    author = article.get_author()

    # updating the number of views
    article.views = article.views + 1
    article.save()

    return render(request,'articles/article_details.htm',{
        'article':article,
        'stories':stories,
        'sections':sections,
        'author':author,
        })

