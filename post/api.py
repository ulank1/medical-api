from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from .models import Post


class PostResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        limit = 0
        max_limit = 0
        queryset = Post.objects.all()
        resource_name = 'post'