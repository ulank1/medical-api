from sqlite3 import IntegrityError

from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.exceptions import BadRequest
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from .models import Post


class UserResource(ModelResource):
    class Meta:
        resource_name = 'user'
        queryset = User.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'id':ALL,
            'username': ALL_WITH_RELATIONS,
            'password': ALL_WITH_RELATIONS,
            'email': ALL_WITH_RELATIONS,
        }

    def obj_create(self, bundle, request=None, **kwargs):

        username, password, email = bundle.data['username'], bundle.data['password'], bundle.data['email']
        try:
            bundle.obj = User.objects.create_user(username=username, password=password, email=email)
        except IntegrityError:
            raise BadRequest('That username already exists')
        return bundle


class PostResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Post.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'post'


