
from rest_framework import serializers
from category.models import Category
from product.models import Product

from product.serializers import ProductSerializer

class CategorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True,source='product')

    class Meta:
        model= Category
        fields = '__all__'