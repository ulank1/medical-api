from sqlite3 import IntegrityError

from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.exceptions import BadRequest

from tastypie.resources import ModelResource

from post.models import Job, Post, Schedule, Appointment


class JobResource(ModelResource):
    class Meta:
        limit = 0
        max_limit = 0
        queryset = Job.objects.all()
        resource_name = 'job'
        allowed_methods = ['get', 'post', 'put', 'delete']


class User1Resource(ModelResource):
    class Meta:
        limit = 0
        max_limit = 0
        queryset = Job.objects.all()
        resource_name = 'user1'
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
                    'name': ALL_WITH_RELATIONS,
                    'surname': ALL,
                    'phone': ALL
                }


class PostResource(ModelResource):
    job = fields.ForeignKey(JobResource, 'job', full=True, null=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Post.objects.all()
        resource_name = 'post'
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'job': ALL_WITH_RELATIONS,
            'name': ALL,
            'surname': ALL
        }


class ScheduleResource(ModelResource):
    doctor = fields.ForeignKey(PostResource, 'doctor', full=True, null=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Schedule.objects.all()
        resource_name = 'schedule'
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'doctor': ALL_WITH_RELATIONS,
            'doctor.job': ALL_WITH_RELATIONS,
            'week_day': ALL
        }


class PoputchikResource(ModelResource):
    doctor = fields.ForeignKey(PostResource, 'doctor', full=True, null=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Appointment.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'search'
        filtering = {
            'doctor': ALL_WITH_RELATIONS,
            'data': ALL,
            'time': ALL,
            'ison': ALL,

        }
