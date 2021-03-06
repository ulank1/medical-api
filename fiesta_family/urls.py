"""fiesta_family URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api

from post.api import PostResource,JobResource,ScheduleResource,PoputchikResource,User1Resource

v1_api = Api(api_name='v1')
v1_api.register(JobResource())
v1_api.register(PostResource())
v1_api.register(PoputchikResource())
v1_api.register(User1Resource())
v1_api.register(ScheduleResource())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
    url(r'^doctor/', 'post.views.home'),
    url(r'^appointment/(?P<doctor>[^/]+)', 'post.views.appointment'),
]
