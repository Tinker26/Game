from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers import *
# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CategoryaViewSet(viewsets.ModelViewSet):
    queryset = Categorya.objects.all()
    serializer_class = CategoryaSerializer
