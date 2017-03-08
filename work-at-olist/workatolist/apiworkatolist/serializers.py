from rest_framework import serializers
from workatolist.models import Channel, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'parent', 'name', 'channel')
        depth = 1

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'parent', 'name', 'channel','subcategories')
        depth = 2

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name')
