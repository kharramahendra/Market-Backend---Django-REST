from .postser import PostSerializer,KeywordSerializer,PostSerializer2
from rest_framework import serializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Contact, Post,Keyword
from django.forms.models import model_to_dict


@api_view(['POST','GET'])
def home(request):
    prices_query = Post.objects.filter(category='Price').order_by('-timestamp')[:6]
    news_query = Post.objects.filter(category='News').order_by('-timestamp')[:4]
    prices = PostSerializer(prices_query,many=True).data
    news = PostSerializer(news_query,many=True).data
    print("no error here")
    return Response({"prices":prices,"news":news})



@api_view(['POST','GET'])
def search(request):
    search_query = request.data.get('slug')
    postcontent= Post.objects.filter(content__icontains=search_query)
    postcategory =Post.objects.filter(category__icontains=search_query)
    allposts_query=  postcontent.union(postcategory)
    all_posts = PostSerializer(allposts_query,many=True).data
    print(all_posts)
    return Response({"posts":all_posts})


@api_view(['POST','GET'])
def single_post(request):
    slug = request.data.get('slug')
    post_query = Post.objects.get(slug=slug)
    post = PostSerializer2(post_query).data
    print(post)
    return Response({"post":post})

@api_view(['POST','GET'])
def contact(request):
    print("api called  ")
    if request.method == 'POST':
        email = request.data.get('email')
        name = request.data.get('name')
        phone = request.data.get('phone')
        message = request.data.get('message')

        print('api called')
        if "@" in str(email) and str(email).endswith('.com'):
            if len(name) > 2 and len(phone) == 10:
                contact = Contact(name=name,email=email,phone=phone,message=message)
                contact.save()
                return Response({"success":True})
            return Response({"success":False,"message":"Too small Name or Phone"})
        return Response({"success":False,"message":"invalid email"})
    
    return Response({"success":False})





@api_view(['POST','GET'])
def prices(request):
    posts_query = Post.objects.filter(category='Price').order_by('-timestamp')
    posts = PostSerializer(posts_query,many=True).data
    return Response({"posts":posts})


@api_view(['POST','GET'])
def news(request):
    posts_query = Post.objects.filter(category='News').order_by('-timestamp')
    posts = PostSerializer(posts_query,many=True).data
    return Response({"posts":posts})