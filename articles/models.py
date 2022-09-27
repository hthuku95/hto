from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# category model
class Category (models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name

# author model
class Author (models.Model):
    name = models.CharField( max_length=50)
    twitter = models.CharField( max_length=100,blank=True,null=True)
    linkedin = models.CharField(max_length=100,blank=True,null=True)

    # snippet utils
    def __str__(self):
        return self.name

# article model
class Article (models.Model):
    title = models.CharField( max_length=50 ,blank=True)
    slug = models.SlugField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(  auto_now_add=True)

    views = models.IntegerField(blank=True,default=0,null=True)

    thumb = models.FileField(blank=True,null=True)
    thumb_description = models.CharField( max_length=50,null=True) 

    categories = models.ForeignKey(Category, blank=True,null=True, on_delete=models.SET_NULL)

    intro = models.TextField( max_length=256, blank=True, null=True)
    outro = models.TextField( max_length=256, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.intro 

    def get_author(self):
        return self.author

# sections model
class Section (models.Model):
    root_article = models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    name = models.CharField( max_length=50, blank=True, null=True)
    heading = models.CharField(blank=True,null=True, max_length=50)
    text_body = models.TextField(blank=True)
    quote = models.TextField(blank=True,null=True)
    code = models.TextField(blank=True,null=True)
    code_language = models.CharField(blank=True,null=True, max_length=50)
    image = models.FileField(blank=True,null=True)
    video = models.FileField(blank=True,null=True)
    link = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("articles:article_details", kwargs={
        'slug': self.slug
    })
    