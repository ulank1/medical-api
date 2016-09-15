from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.exceptions import BadRequest

from tastypie.resources import ModelResource

from post.models import Post, User


class UserResource(ModelResource):
    class Meta:
        resource_name = 'user_new'
        queryset = User.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'id':ALL,
            'username': ALL,
            'password': ALL,
            'email': ALL,
        }


class PostResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Post.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'post'
        filtering = {
            'category': ALL,
            'title': ALL,
            'description': ALL,
            'email': ALL,
        }