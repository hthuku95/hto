from django.db import models
from profiles.models import UserProfile

# Create your models here.

STATUS_CHOICES = (
    ('A','Approved'),
    ('D','Denied'),
    ('IQ','In Que')
)

PRIORITY_CHOICES = (
    ('HS','Highly Sensitive'),
    ('S','Sensitive'),
    ('M','Medium Priority'),
    ('L','Low Priority'),
    ('LT','Long Term')
)

class ImprovementProposal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default='IQ')
    title = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, blank=True, null=True, max_length=2)
    deadline = models.DateTimeField(blank=True,null=True)

    def __str__(self): 
        return self.title
    


class ArticleIdea(models.Model ):
    title = models.CharField(max_length=256)

class SubTitle(models.Model):
    article_idea = models.ForeignKey(ArticleIdea, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

