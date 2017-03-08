from rest_framework import serializers
from workatolist.models import Channel, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'parent', 'name', 'channel')

class CategoryParentSerializer(serializers.ModelSerializer):
    parent = CategorySerializer(read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'parent', 'name', 'channel')


class CategorySimpleSerializer(serializers.ModelSerializer):
    parent = CategoryParentSerializer(read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'parent', 'name', 'channel','subcategories')

class CategoryDetailSerializer(serializers.ModelSerializer):
    subcategories = CategorySimpleSerializer(many=True, read_only=True)
    parent = CategorySerializer(read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'parent', 'name', 'channel','subcategories')

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name')
