from django.db import models
from profiles.models import UserProfile

# Create your models here.

NEWS_PLAN_CHOICES = (
    ('D','Daily'),
    ('W','Weekly'),
    ('M','Monthly')
)

# contact model
class Contact (models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name

class Email(models.Model):
    # Add the option to change the news_plan inside the email
    user = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
    email = models.EmailField(blank=True,null=True, max_length=254)
    news_plan = models.CharField(blank=True,null=True,choices=NEWS_PLAN_CHOICES,default='D', max_length=2)
 
    def __str__(self):
        return self.email
    