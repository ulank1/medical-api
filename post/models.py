# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    extra_phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    choices = (('Муж', 'Муж'), ('Жен', 'Жен'))
    sex = models.CharField(choices=choices, max_length=10)
    email = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.username


class Poputka(models.Model):
    user = models.ForeignKey(User, verbose_name='user', null=True)
    choices = (('легковая', 'легковая'), ('грузовая', 'грузовая'))
    type_of_car = models.CharField(max_length=20, choices=choices)
    car_number = models.CharField(max_length=10, null=True)
    car_model = models.CharField(max_length=30, null=True)
    date = models.CharField(max_length=50)
    point_a = models.CharField(max_length=50)
    point_b = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=750)
    price = models.CharField(max_length=10)
    choices2 = (('по стране', 'по стране'), ('по городу', 'по городу'), ('по миру', 'по миру'))
    type_of_motion = models.CharField(max_length=20, choices=choices2)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.title


class Poputchik(models.Model):
    user = models.ForeignKey(User, verbose_name='user', null=True)
    date = models.CharField(max_length=50)
    point_a = models.CharField(max_length=50)
    point_b = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=750)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.title
