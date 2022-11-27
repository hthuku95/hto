from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path(r'',views.article_list, name= 'article_lists'),
    path(r'<year>/<month>/<day>/<slug>/',views.article_details, name='article_details'),
    path(r'category/<slug>/',views.article_category, name= 'article_category'),
]