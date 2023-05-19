from django_filters import rest_framework as filters
from .serializers import CommentSerializer, StarsSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Comment, Stars
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     # Apply additional filters based on query parameters
    #     category = self.request.query_params.get('title')
    #     if category:
    #         queryset = queryset.filter(category=category)
    #
    #     return queryset


# class ProductFilter(filters.FilterSet):
#     category = filters.DjangoFilterBackend()
#
#     class Meta:
#         model = Product
#         fields = ['category__id']
#
#
# class ProductPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100


class StarsModelViewSet(ModelViewSet):
    queryset = Stars.objects.all()
    serializer_class = StarsSerializer
    # filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    # search_fields = ['title']  # Fields to enable searching
    # ordering_fields = ['title']
    # filterset_class = ProductFilter
    # pagination_class = ProductPagination

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return GetProductSerializer
    #     return ProductSerializer
from django.shortcuts import render

# Create your views here.
