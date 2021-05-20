from rest_framework import serializers

from .models import Category, Furniture


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ["id", "category", "name", "price", "material","size","image", "description"]
