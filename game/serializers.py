from rest_framework import serializers
from .models import *

class KomandalarSerializer(serializers.ModelSerializer):
    class Meta():
        model = Komandalar
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta():
        model = Blog
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    category = KomandalarSerializer(read_only=True, many=True)
    categorya = BlogSerializer(read_only=True, many=True)

    class Meta():
        model = Category
        fields = '__all__'


