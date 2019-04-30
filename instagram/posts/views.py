from django.shortcuts import render

# Create your views here.

from posts.models import Posts
from posts.serializers import UserSerializer

from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = UserSerializer