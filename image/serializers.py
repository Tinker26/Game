from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta():
        model = Image
        fields = '__all__'



class CategoryasSerializer(serializers.ModelSerializer):
    category = ImageSerializer(read_only=True, many=True)

    class Meta():
        model = Categoryas
        fields = '__all__'
