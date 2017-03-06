from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'channels', views.ChannelViewSet)
router.register(r'channels/(?P<id>\d+)/categories', views.ChannelCategoriesDetailViewSet,
    base_name = 'channel-categories-detail')
router.register(r'categories', views.CategoryViewSet)
