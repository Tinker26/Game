from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers import *
# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class CategoryasViewSet(viewsets.ModelViewSet):
    queryset = Categoryas.objects.all()
    serializer_class = CategoryasSerializer
