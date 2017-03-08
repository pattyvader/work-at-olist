from rest_framework import authentication, permissions, viewsets
from workatolist.models import Channel, Category
from workatolist.apiworkatolist.serializers import ChannelSerializer, CategorySerializer, CategoryDetailSerializer

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        id = self.kwargs['id']

        return Category.objects.filter(id = id)

class ChannelCategoriesDetailViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Category.objects.filter(channel_id = id)
