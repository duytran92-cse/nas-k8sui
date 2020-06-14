
from django.conf.urls import include, url
from . import actions

urlpatterns = [
    url(r'^list$',                                         actions.List.as_view(),     name='namespaces_services_list'),
    url(r'^view/(?P<name>([A-Za-z0-9\-\_]+))',             actions.View.as_view(),     name='namespaces_services_view'),
]
