from __future__ import unicode_literals
from django.db import models

class Channel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_id = models.IntegerField(blank=True, null=True)
    channel = models.ForeignKey('Channel', on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('channel', args=[str(self.id)])
