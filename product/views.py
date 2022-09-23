from django.http import Http404
from rest_framework.parsers import JSONParser
from .models import Product, Category
from .serializers import ProductSerializer, CartSerializer, UpdateSerializer
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Cart, Product
from .serializers import CategorySerializer
from django.core.paginator import Paginator


class ProductListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self,  request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CartCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializers = CartSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCartAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get(self, request, id):
        cart = Cart.objects.get(user_id=id)
        product = cart.product.all()
        serializer = CartSerializer(cart)
        serializer2 = ProductSerializer(product, many=True)
        data = serializer.data
        data['product'] = serializer2.data
        return Response(data)

    def put(self, requests,id):
        cart = Cart.objects.get(user_id=id)
        serializer = UpdateSerializer(cart, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AddCartAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#     parser_classes = [JSONParser]
#     def post(self, request):
#         serializers = CartSerializer(data=request.data)
#         if serializers.is_valid():
#            serializers.save()
#            return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductDetailApiView(APIView):
#
#     def get_object(self, id):
#         try:
#             return Product.objects.get(id=id)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def get(self, request, id):
#         post = self.get_object(id)
#         serializers = ProductSerializer(post)
#         data = serializers.data
#         return Response(data)
#
#
# class ProductUpdateApiView(APIView):
#     permission_classes = [permissions.AllowAny]
#     def get_object(self, id):
#         try:
#             return Product.objects.get(id=id)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def put(self, requests,id):
#         post = self.get_object(id)
#         serializer = ProductSerializer(post, data=requests.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProductDestroyApiView(APIView):
#
#     def get_object(self, id):
#         try:
#             return Product.objects.get(id=id)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def delete(self, requests, id):
#         post = self.get_object(id)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class CategoryListApiView(APIView):
#     def get(self, request):
#         products = Category.objects.all()
#         serializers = CategorySerializer(products, many=True)
#         return Response(serializers.data)
#
#
# class MaxPriceListApiView(APIView):
#
#     def get(self, request):
#         products = Product.objects.all()
#         names = Product.objects.all()
#         price_list = []
#         revenue = []
#         for j in products:
#             one = j.price * j.quantity
#             price_list.append(j.price)
#             revenue.append(one)
#         post_count = len(price_list)
#         revenue = sum(revenue)
#         max_price = max(price_list)
#         avg_price = sum(price_list) / len(price_list)
#         min_price = min(price_list)
#         data = {
#             "max_price": max_price,
#             "avg_price": avg_price,
#             "min_price": min_price,
#             "revenue": revenue,
#             "number of posts": post_count
#
#         }
#         return Response(data)
#
#
# class CategoryCreateApiView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         serializers = CategorySerializer(data=request.data)
#         if serializers.is_valid():
#            serializers.save()
#            return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CategoryDetailApiView(APIView):
#     permission_classes = [permissions.AllowAny]
#     parser_classes = [JSONParser]
#
#     def get_object(self, name):
#         try:
#             return Category.objects.get(name=name)
#         except Category.DoesNotExist:
#             raise Http404
#
#     def get(self, request, name):
#         category = self.get_object(name)
#         product = Product.objects.filter(category__name=name)
#         serializer = CategorySerializer(category)
#         serializer2 = ProductSerializer(product, many=True)
#         data = serializer.data
#         data['products'] = serializer2.data
#
#         return Response(data)
#
#
# class CategoryUpdateApiView(APIView):
#
#     permission_classes = [permissions.AllowAny]
#     def get_object(self, id):
#         try:
#             return Category.objects.get(id=id)
#         except Category.DoesNotExist:
#             raise Http404
#
#     def put(self, requests,id):
#         post = self.get_object(id)
#         serializer = CategorySerializer(post, data=requests.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CategoryDestroyApiView(APIView):
#
#     def get_object(self, id):
#         try:
#             return Category.objects.get(id=id)
#         except Category.DoesNotExist:
#             raise Http404
#
#     def delete(self, requests, id):
#         post = self.get_object(id)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)