from __future__ import unicode_literals

from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User, verbose_name='user', null=True)
    category = models.CharField(max_length=20)
    photo_url = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=750)
    price = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.category
