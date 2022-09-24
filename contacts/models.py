from django.db import models

# Create your models here.
#contact model
class Contact (models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    message = models.TextField()

    #snippet utils
    def __str__(self):
        return self.name