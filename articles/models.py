from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from profiles.models import UserProfile
# Create your models here.
# category model
class Category (models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("articles:article_category",kwargs={
            'slug':self.name
        })
        
# author model
class Author (models.Model):
    user = models.ForeignKey(UserProfile, blank=True,null=True, on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    twitter = models.CharField( max_length=100,blank=True,null=True)
    linkedin = models.CharField(max_length=100,blank=True,null=True)
    twitter_handle = models.CharField(max_length=50,default="Username should start with @")

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name

# article model
class Article (models.Model):
    title = models.CharField( max_length=512 ,blank=True)
    slug = models.SlugField(max_length=512)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(  auto_now_add=True)

    views = models.IntegerField(blank=True,default=0,null=True)

    thumb = models.FileField(blank=True,null=True)
    thumb_description = models.CharField( max_length=512,null=True) 

    # Populate the DB with many tags and rotate them 
    tags = models.ManyToManyField(Tag, blank=True)

    category = models.ForeignKey(Category, blank=True,null=True, on_delete=models.SET_NULL)
    summary = models.TextField(default="Article summary")
    intro = models.TextField(blank=True, null=True)
    outro = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_author(self):
        return self.author

    def get_absolute_url(self):
        return reverse("articles:article_details", kwargs={
            'year':self.date.year,
            'month':self.date.month,
            'day':self.date.day,
            'slug': self.slug
        })

# sections model
class Section (models.Model):
    root_article = models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    heading = models.CharField(blank=True,null=True, max_length=512)
    text_body = models.TextField(blank=True)
    quote = models.TextField(blank=True,null=True)
    code = models.TextField(blank=True,null=True)
    code_language = models.CharField(blank=True,null=True, max_length=50)
    image = models.FileField(blank=True,null=True)
    video = models.FileField(blank=True,null=True)

    def __str__(self):
        return self.name




    