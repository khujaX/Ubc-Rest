from .models import News, Category, User
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from . import serializers
from rest_framework import viewsets
from .permissions import *
from .paginations import NewsResultPagination
from rest_framework.parsers import MultiPartParser


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
    pagination_class = NewsResultPagination

class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
    pagination_class = NewsResultPagination

class NewsCreate(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsCreateSerializer
    permission_classes = (CanCreateNews,)
    parser_classes = (MultiPartParser,)


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer


class NewsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsCreateSerializer
    permission_classes = (IsPublisherOrReadOnly,)
    parser_classes = (MultiPartParser,)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticated, IsSuperUser)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (CanUpdateProfile,)


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (CanUpdateProfile,)


