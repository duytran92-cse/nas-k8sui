
from django.conf.urls import include, url
from . import actions

urlpatterns = [
    #insert deployment url here
    url(r'^create$',                                        actions.Create.as_view(),   name='namespaces_deployments_create'),
    url(r'^list$',                                          actions.List.as_view(),  	name='namespaces_deployments_list'),
    url(r'^view/(?P<name>([A-Za-z0-9\-\_]+))',              actions.View.as_view(),    	name='namespaces_deployments_view'),
]
