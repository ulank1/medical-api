# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Poputka(models.Model):
    price = models.CharField(max_length=10)
    lat = models.FloatField()
    longt = models.FloatField()
    loc = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.price


class Poputchik(models.Model):
    price = models.CharField(max_length=10)
    lat = models.FloatField()
    longt = models.FloatField()
    loc = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.price
