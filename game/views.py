from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers import *
# Create your views here.
class KomandalarViewSet(viewsets.ModelViewSet):
    queryset = Komandalar.objects.all()
    serializer_class = KomandalarSerializer
    # pagination_class = LargeResultsSetPagination
    # filter_backends = [filters.OrderingFilter,DjangoFilterBackend,filters.SearchFilter]
    # ordering_fields = ['name','price']
    # ordering = ['price']
    # search_fields = ['^name']
    # filterset_fields = ['name','price']
    # pagination_class = LimitOffsetPagination

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer