from django.db.models import fields
from .models import Keyword
# from requests.models import ReadTimeoutError
from rest_framework import serializers, validators
from .models import Post


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['choice']
    def to_representation(self, value):
         return value.choice

class PostSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True,read_only=True)
    timestamp=serializers.DateTimeField(format="%d %b, %Y %A")
    class Meta:
        model = Post
        fields = ['sno','slug','title','keywords','category','timestamp','image','image_url']
        depth = 1 
class PostSerializer2(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True,read_only=True)
    timestamp=serializers.DateTimeField(format="%d %b, %Y %A")
    class Meta:
        model = Post
        fields = ['sno','slug','title','content','keywords','category','timestamp','image','image_url']
        depth = 1 
