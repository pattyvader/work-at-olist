from __future__ import unicode_literals
from django.db import models

class Channel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    managed=True

    def __str__(self):
        return self.name

    def count_channel(self, name_channel):
        number_channel = Channel.objects.filter(name = name_channel).count()

        return number_channel

    def get_channel(self, channel_name):
        channel = Channel.objects.get(name = channel_name)

        return channel

class CategoryManager(models.Manager):
    def create_category(self, name, parent, channel):
        category = self.create(name = name, parent = parent, channel = channel)

        return category

class Category(models.Model):
    name = models.CharField(max_length=100)
    channel = models.ForeignKey('Channel', on_delete=models.SET_NULL,null=True,related_name='categories')
    parent = models.ForeignKey('self',null=True, blank=True,related_name='subcategories')
    managed=True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('channel', args=[str(self.id)])

    objects = CategoryManager()
