from sqlite3 import IntegrityError

from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.exceptions import BadRequest

from tastypie.resources import ModelResource

from post.models import Poputka, Poputchik


class PoputkaResource(ModelResource):
    class Meta:
        limit = 0
        max_limit = 0
        queryset = Poputka.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'route'
        filtering = {
            'price': ALL
        }


class PoputchikResource(ModelResource):
    class Meta:
        limit = 0
        max_limit = 0
        queryset = Poputchik.objects.all()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'search'
        filtering = {
            'price': ALL

        }
