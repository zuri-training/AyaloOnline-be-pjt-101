from rest_framework import serializers
from .models import Category, Product




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'title')
        model = Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude=['status', 'picture']

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

