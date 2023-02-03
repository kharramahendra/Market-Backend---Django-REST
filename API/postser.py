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
    timestamp=serializers.DateTimeField(format="%a %b %d, %Y")
    class Meta:
        model = Post
        fields = ['sno','content','slug','title','keywords','timestamp','image','image_url']
        depth = 1 
       
