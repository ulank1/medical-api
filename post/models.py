# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Job(models.Model):
    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'должности'

    job = models.CharField(max_length=20, null=True, verbose_name='должность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.job


class Post(models.Model):
    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    job = models.ForeignKey(Job, verbose_name='должность', null=True)
    name = models.CharField(max_length=100, verbose_name='имя', null=True)
    surname = models.CharField(max_length=100, verbose_name='фамилия', null=True)
    experience = models.IntegerField(verbose_name='опыт', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)


class Appointment(models.Model):
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
    doctor = models.ForeignKey(Post, verbose_name='врач', null=True)
    time = models.CharField(max_length=100, verbose_name='время',null=True)
    name = models.CharField(max_length=100, verbose_name='имя', null=True)
    surname = models.CharField(max_length=100, verbose_name='фамилия', null=True)
    number = models.CharField(max_length=100, verbose_name='номер телефона', null=True)
    data = models.CharField(max_length=100, verbose_name='дата', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return '%s %s' % (self.data, self.doctor.name)


class Schedule(models.Model):
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    doctor = models.ForeignKey(Post, verbose_name='врач', null=True)
    time_from = models.CharField(max_length=100, verbose_name='от', null=True)
    time_to = models.CharField(max_length=100, verbose_name='до', null=True)
    week_day = models.CharField(max_length=100, verbose_name='день недели', null=True)
    ison = models.CharField(max_length=100, verbose_name='ison', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __unicode__(self):
        return self.doctor.name


