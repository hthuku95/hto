from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from .models import Article, Category, Section
from django.contrib import messages
from contacts.models import Contact,Email
from contacts.forms import NewsletterForm
from profiles.models import UserProfile
# Create your views here.

# article category page
def article_category(request, slug):
    articles = Article.objects.filter(category__name = slug).order_by('-date')
    categories = Category.objects.all()

    context = {
        'articles':articles,
        'categories':categories
    }

    return render(request,'articles/article_category.html',context)

# article list page
def article_list(request):
    articles = Article.objects.all().order_by('-date')
    categories = Category.objects.all()

    context = {
        'articles':articles,
        'categories':categories
    }

    return render(request,'articles/article_list.html',context)

# article details
def article_details(request,slug, *args, **kwargs):
    article = Article.objects.get(slug=slug)
    stories = Article.objects.filter(category=article.category).exclude(slug=slug).order_by('date')[:4]
    sections = Section.objects.filter(root_article=article).order_by('section_number')
    author = article.get_author()
    categories = Category.objects.all()

    # updating the number of views
    article.views = article.views + 1
    article.save()


    if request.method == 'POST':
        form = NewsletterForm(request.POST)

        if form.is_valid():
            email_address = form.cleaned_data['email']

            email_address_qs = Email.objects.filter(email=email_address)
            if email_address_qs.exists():
                messages.info(request, "You are already subscribed")
                return redirect("articles:article_details",slug=article.slug)
            else:
                new_email = Email(user=user,email=email_address)
                new_email.save()
                messages.success(request, "Email address added successfully")
                return redirect("articles:article_details",slug=article.slug)
    else:
        form = NewsletterForm()
    
    context = {
        'article':article,
        'stories':stories,
        'sections':sections,
        'author':author,
        'form':form,
        'categories':categories
        }

    return render(request,'articles/article_details.html',context)

