from .models import Product, Cart, Category
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'user', 'price', 'description', 'created_date', 'quantity']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'product']


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product']
