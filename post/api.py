from sqlite3 import IntegrityError


from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.exceptions import BadRequest

from tastypie.resources import ModelResource

from post.models import Poputka, User, Poputchik


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


class PoputkaResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Poputka.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'poputka'
        filtering = {
            'point_a': ALL,
            'point_b': ALL,
            'title': ALL_WITH_RELATIONS,
            'type_of_car': ALL,
            'type_of_motion': ALL,
            'date': ALL,
        }


class PoputchikResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user', null=True, full=True)

    class Meta:
        limit = 0
        max_limit = 0
        queryset = Poputchik.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'poputchik'
        filtering = {
            'point_a': ALL,
            'point_b': ALL,
            'title': ALL_WITH_RELATIONS,
        }