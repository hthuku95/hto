
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('articles/',include('articles.urls')),
    path(r'',views.index_view),
]

# appending the static files urls to the above media
urlpatterns += staticfiles_urlpatterns()
# how to upload media..appending the media url to the patterns above
