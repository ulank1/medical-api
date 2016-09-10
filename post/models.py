from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, verbose_name='user', null=True, blank=True)
    description = models.TextField(max_length=1000)
    address = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    title = models.CharField(max_length=100,null=True)

    def __unicode__(self):
        return self.description

