from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers import *
# Create your views here.
class KomandalarViewSet(viewsets.ModelViewSet):
    queryset = Komandalar.objects.all()
    serializer_class = KomandalarSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer