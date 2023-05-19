from rest_framework import serializers
from .models import Comment, Stars


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'customer', 'product', 'datetime',)
        extra_kwargs = {
            'datetime': {'read_only': True}
        }


class StarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stars
        fields = ('id', 'rating', 'customer', 'product', 'datetime',)
        extra_kwargs = {
            'datetime': {'read_only': True}
        }

# class GetProductSerializer(serializers.ModelSerializer):
#     category = CategorySerializer(read_only=True)
#     class Meta:
#         model = Product
#         fields = ('id', 'title', 'description', 'price', 'image', 'category',)