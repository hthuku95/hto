from django.contrib import admin
from .models import Article,Category,Author,Section,Tag,ListItem

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Section)
admin.site.register(Tag)
admin.site.register(ListItem)

