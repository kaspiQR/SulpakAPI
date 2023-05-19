from rest_framework import serializers
from .models import Category, Product
from ..reviews.serializers import CommentSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'image', 'category', 'product_comments',)


class GetProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    product_comments= CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'image', 'category', 'product_comments', 'get_rating',)
