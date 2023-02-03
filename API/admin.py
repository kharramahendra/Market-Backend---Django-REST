from django.contrib import admin

from .models import Contact, Keyword, Post

# Register your models here.
admin.site.register(Keyword)
admin.site.register(Contact)
@admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     class Media:
#         js = ('tinyInject.js')

class Post(admin.ModelAdmin):
    model = Post
    filter_horizontal = ('keywords',)