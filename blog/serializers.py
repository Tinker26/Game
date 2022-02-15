from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.ModelSerializer):
    class Meta():
        model = Blog
        fields = '__all__'

class CategoryaSerializer(serializers.ModelSerializer):
    categoryas = BlogSerializer(read_only=True, many=True)

    class Meta():
        model = Categorya
        fields = '__all__'