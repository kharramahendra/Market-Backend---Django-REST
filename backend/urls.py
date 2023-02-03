
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import include, path, re_path

from API import views
from django.conf import settings
admin.site.site_header = "Tensorcodes"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('news/',views.news),
    path('prices/',views.news),

    path('search/',views.search),
    path('contact/',views.contact),

    path('singlepost/',views.single_post),

    
    # 
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)#STATICFILES_DIRS[0])
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT[0])