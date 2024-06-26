from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product


class ProductListAPIView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        products = Product.objects.all()
        paginator = Paginator(products, 5)
        page = paginator.get_page(paginator)
        serializer = ProductSerializer(page, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['author'] = request.user.id
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductDetailAPIView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)
    
    def get(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(pk=pk)
        if request.user != product.author:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        request.data['author'] = request.user.id
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, pk):
        product = self.get_object(pk=pk)
        if request.user != product.author:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        product.delete()
        data = {"delete": f"{pk} is deleted."}
        return Response(data, status=status.HTTP_200_OK)