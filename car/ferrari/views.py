from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class PostList (generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail (generics.REtrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    Serializer = PostSerializer

# Create your views here.
