from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.core.cache import cache

class ProductListAPIView(APIView):
    def get(self, reqeust):
        ## 모든 상품 조회
        cache_key = "product_list"
        if not cache.get(cache_key):
            print("cache miss")
            products = Product.objects.all()
            serializers = ProductSerializer(products, many=True)
            json_response = serializers.data
            cache.set("product_list", json_response, 100)
        json_response = cache.get(cache_key)
        return Response(json_response)
