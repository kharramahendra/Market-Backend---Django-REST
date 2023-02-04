from ast import keyword
from importlib.resources import contents
from random import choices
from tokenize import blank_re
from unicodedata import category
from django.db import models
# from traitlets import default
# from multiselectfield import MultiSelectField #problem hai 
from django.utils.timezone import now
from tinymce.models import HTMLField 
from django.template.defaultfilters import slugify
import datetime
# from ckeditor.fields import RichTextField as HTMLField
now = datetime.datetime.now()

category_choices =(
    ("News", "News"),
    ("Price", "Price"),
)



class Keyword(models.Model):
    choice = models.CharField(max_length=154, unique=True)

    def __str__(self):
        return self.choice

import random
# print(random.randint(0, 9))


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=2000)
    slug =  models.SlugField(blank=True,unique=True,max_length=255)
    content = HTMLField(default="")
    category =  models.CharField(max_length = 50,choices = category_choices,default = '1')
    keywords = models.ManyToManyField(Keyword)
    timestamp=models.DateTimeField(default=now,blank=True)
    image = models.ImageField(upload_to='postimages',blank=True,null=True)
    image_url = models.CharField(max_length=1000,default="",blank=True)

    def save(self, *args, **kwargs):
        self.slug = str(str(self.title) +""+str(self.category)+str(random.randint(0, 99))+str(self.sno))[0:48] 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50,blank=True)
    email = models.CharField(max_length=50,blank = True)
    phone = models.CharField(max_length=13,blank=True)
    message = models.CharField(max_length=2000,blank=True)
    plan = models.CharField(max_length = 10,blank=True)

    def __stt__(self):
        return self.name
